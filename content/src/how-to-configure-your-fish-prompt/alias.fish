# Replace ls with eza
alias ls 'eza -al --color=always --group-directories-first --icons' # preferred listing
alias la 'eza -a --color=always --group-directories-first --icons'  # all files and dirs
alias ll 'eza -l --color=always --group-directories-first --icons'  # long format
alias lt 'eza -aT --color=always --group-directories-first --icons' # tree listing
alias l. "eza -a | grep -e '^\.'"                                     # show only dotfiles
alias ls 'eza --color=always --group-directories-first --icons'

# Common use
alias psmem 'ps auxf | sort -nr -k 4'
alias psmem10 'ps auxf | sort -nr -k 4 | head -10'
alias .. 'cd ..'
alias ... 'cd ../..'
alias .... 'cd ../../..'
alias ..... 'cd ../../../..'
alias ...... 'cd ../../../../..'
alias dir 'dir --color=auto'
alias vdir 'vdir --color=auto'
alias grep 'grep --color=auto'
alias fgrep 'fgrep --color=auto'
alias egrep 'egrep --color=auto'
alias hw 'hwinfo --short'                                   # Hardware Info

# Get the error messages from journalctl
alias jctl "journalctl -p 3 -xb"

# root commands
alias dnf 'sudo dnf'
alias reboot 'sudo reboot'
alias shutdown 'sudo systemctl shutdown'
alias update 'sudo dnf --refresh update'
alias yum 'sudo dnf'

# use vim
alias vi vim
# include alias in the `which` command
alias which 'alias | /usr/bin/which --tty-only --read-alias --read-functions --show-tilde --show-dot'
