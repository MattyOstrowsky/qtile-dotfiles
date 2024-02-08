export PATH=$HOME/bin:/usr/local/bin:$PATH
export ZSH="$HOME/.oh-my-zsh"
export PATH=$PATH:/usr/local/go/bin
export PATH=/home/mat/.local/bin:$PATH

ZSH_THEME="robbyrussell"

plugins=(git zsh-autosuggestions zsh-fzf-history-search zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

eval "$(starship init zsh)"

neofetch

autoload -U +X bashcompinit && bashcompinit
complete -o nospace -C /usr/bin/terraform terraform
