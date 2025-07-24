""set nocompatible
syntax enable
set background=light
"colorscheme solarized
filetype on
filetype plugin on
filetype indent on

set splitbelow
set splitright
set autowrite
set number

nnoremap <F2> ZZ
""map <F3> gg=G 
nnoremap <F6> :tabp <CR>
nnoremap <F7> :tabn <CR>
inoremap <F8> <C-P>
inoremap <F9> <C-N>
nnoremap <F12> :w<CR>

"inoremap <ESC> <ESC>:w<CR> "why does this break my arrow keys in terminal mode?

nnoremap <F8> <C-w>h
nnoremap <F9> <C-w>l

""nnoremap <Right> <C-w>l
""nnoremap <Left> <C-w>h
""nnoremap <Up> <C-w>k
""nnoremap <Down> <C-w>j

let @v = 'i$()'



