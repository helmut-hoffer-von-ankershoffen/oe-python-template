#!/bin/sh
# shellcheck shell=sh

echo "Installing dev tools to enable project management with oe-python-template and derivatives ..."

# Define tool lists as strings with delimiters for cross-platform compatibility
LINUX_APT_TOOLS="curl;curl;https://curl.se/"

BREW_TOOLS="uv;uv;https://docs.astral.sh/uv/
git;git;https://git-scm.com/
gpg;gnupg;https://gnupg.org/
gmake;make;https://www.gnu.org/software/make/
jq;jq;https://jqlang.org/
xmllint;libxml2;https://en.wikipedia.org/wiki/Libxml2
act;act;https://nektosact.com/
pinact;pinact;https://github.com/suzuki-shunsuke/pinact
trivy;trivy;https://trivy.dev/latest/
pnpm;pnpm;https://pnpm.io/
magick;imagemagick;https://imagemagick.org/
nixpacks;nixpacks;https://nixpacks.com/"

MAC_BREW_TOOLS="pinentry-mac;pinentry-mac;https://github.com/GPGTools/pinentry"

LINUX_BREW_TOOLS=""

UV_TOOLS="copier;copier;https://copier.readthedocs.io/"

# Function to install/update brew tools
install_or_upgrade_brew_tool() {
    local tool=$1
    local package=$2
    local url=$3

    if command -v "$tool" > /dev/null 2>&1; then
        tool_path=$(command -v "$tool")
        case "$tool_path" in
            *brew/*)
                echo "$tool already installed via Homebrew at $tool_path, upgrading..."
                brew upgrade "$package" || true
                ;;
            *)
                echo "$tool already installed at $tool_path, skipping..."
                ;;
        esac
    else
        echo "Installing $tool from $package... # $url"
        brew install "$package"
    fi
}

# Function to install/update Linux tools via apt
install_or_update_linux_apt_tool() {
    local tool=$1
    local package=$2
    local url=$3

    if command -v "$tool" > /dev/null 2>&1; then
        echo "$tool already installed at $(command -v "$tool"), skipping..."
    else
        echo "Installing $tool... # $url"
        sudo apt-get update -y && sudo apt-get install "$package" -y
    fi
}

# Function to install/update tools via uv
install_or_update_uv_tool() {
    local tool=$1
    local url=$3

    if command -v "$tool" > /dev/null 2>&1; then
        echo "$tool already installed at $(command -v "$tool"), updating..."
        uv tool update "$tool"
    else
        echo "Installing $tool... # $url"
        uv tool install "$tool"
    fi
}

# Install/update Linux packages
if [ "$(uname -s | cut -c1-5)" = "Linux" ]; then
    echo "$LINUX_APT_TOOLS" | while IFS=';' read -r tool package url; do
        [ -n "$tool" ] && install_or_update_linux_apt_tool "$tool" "$package" "$url"
    done
fi

# Install/update Homebrew itself
if ! command -v brew > /dev/null 2>&1; then
    echo "Installing Homebrew... # https://brew.sh/"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to PATH based on platform
    if [ "$(uname -s)" = "Darwin" ]; then
        # macOS - Homebrew path setup
        if [ "$(uname -m)" = "arm64" ]; then
            # M1/M2 Mac
            eval "$(/opt/homebrew/bin/brew shellenv)"
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> "$HOME/.zprofile"
        else
            # Intel Mac
            eval "$(/usr/local/bin/brew shellenv)"
            echo 'eval "$(/usr/local/bin/brew shellenv)"' >> "$HOME/.zprofile"
        fi
    elif [ "$(uname -s | cut -c1-5)" = "Linux" ]; then
        # Linux - Homebrew path setup
        if [ -d "$HOME/.linuxbrew" ]; then
            eval "$($HOME/.linuxbrew/bin/brew shellenv)"
        fi
        if [ -d "/home/linuxbrew/.linuxbrew" ]; then
            eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
        fi
        brew_prefix=$(brew --prefix 2>/dev/null || echo "/home/linuxbrew/.linuxbrew")
        echo "eval \$(${brew_prefix}/bin/brew shellenv)" >> "$HOME/.bashrc"
    fi
else
    echo "Homebrew already installed at $(command -v brew), updating..."
    brew update
fi

# Install/update Homebrew tools
echo "$BREW_TOOLS" | while IFS=';' read -r tool package url; do
    [ -n "$tool" ] && install_or_upgrade_brew_tool "$tool" "$package" "$url"
done

# Install/update Homebrew tools for macOS
if [ "$(uname -s)" = "Darwin" ]; then
    echo "$MAC_BREW_TOOLS" | while IFS=';' read -r tool package url; do
        [ -n "$tool" ] && install_or_upgrade_brew_tool "$tool" "$package" "$url"
    done
fi

# Install/update Homebrew tools for Linux
if [ "$(uname -s | cut -c1-5)" = "Linux" ]; then
    echo "$LINUX_BREW_TOOLS" | while IFS=';' read -r tool package url; do
        [ -n "$tool" ] && install_or_upgrade_brew_tool "$tool" "$package" "$url"
    done
fi

# Install/update UV tools
echo "$UV_TOOLS" | while IFS=';' read -r tool package url; do
    [ -n "$tool" ] && install_or_update_uv_tool "$tool" "$url"
done
