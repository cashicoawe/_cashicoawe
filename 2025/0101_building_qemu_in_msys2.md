# building qemu in msys2

virgl 対応した qemu を msys2 上でビルドした作業ログ 

virgl はわからないけど whpx は顕著な差が出るので幸せ  
オプション次第でエラーが出るので、そもそもバイナリで問題なかった可能性

# 結論

msys2 をダウンロード  
https://www.msys2.org/

msys2 の symlink 作成を許可する  
- ucrt64.ini の "#MSYS=winsymlinks:nativestrict" の先頭 "#" を削除する  
- windows の開発者モードを有効化する

qemu をビルド
```
# ucrt64.exe

pacman -Syu
pacman -S base-devel git mingw-w64-ucrt-x86_64-virglrenderer

# qemu のソースをダウンロード
git clone https://github.com/msys2/MINGW-packages
cd MINGW-packages/mingw-w64-qemu

# いろいろ有効化してビルド
CONFIGURE_OPTS="--enable-gtk-clipboard --enable-opengl --enable-virglrenderer" \  
makepkg -sCLf --skippgpcheck --nocheck --noconfirm

# インストール
# バージョンは適当に読み替えてください
pacman -U \
mingw-w64-ucrt-x86_64-qemu-*-any.pkg.tar.zst \
mingw-w64-ucrt-x86_64-qemu-common-*-any.pkg.tar.zst \
mingw-w64-ucrt-x86_64-qemu-image-util-*-any.pkg.tar.zst \
```

# alpine linux 使用例

インストール用イメージを入手する  
https://alpinelinux.org/downloads/  

msys2 のルートディレクトリ下に適当な名前で配置しておく  
今回は "alpine.iso"  
また、インストール先イメージは "alpine.qcow2"

インストール先イメージの起動  

```
# ucrt64.exe

qemu-img create -f qcow2 alpine.qcow2 10G
qemu-system-x86_64 \
    -smp 2 \
    -m 4G \
    -drive format=qcow2,file=alpine.qcow2,if=virtio \
    -boot once=d \
    -cdrom alpine.iso
```

ほっといたら起動する  
ユーザーは root  

alpine.qcow2 に alpine linux をインストールする  
setup-alpine使えば何事もなく終わる  
ネットワーク特に設定してないけどなぜ動いたよ

```
# alpine installer

setup-alpine
```

大体エンターでいい  
インストール先の選択が面倒ぐらい  
終わったらシャットダウンする

```
# alpine installer

poweroff
```

windows で whpx を有効にする  
```
# コントロールパネル

プログラム ->
windowsの機能の有効化または無効化 -> 
Windows ハイパーバイザー プラットフォーム
```
whpx アクセラレーションおよび virgl を有効化して起動する

```
# ucrt64.exe

qemu-system-x86_64 \
    -smp 4 \
    -m 10G \
    -drive format=qcow2,file=alpine.qcow2,if=virtio \
    -device virtio-vga-gl \
    -display sdl,gl=on \
    -accel whpx,kernel-irqchip=off
```

# errors

オプション適当に試すしかない  
0101/makefile に検証した奴らがあるのでそっち確認してください

- segmentation fault
    - わからん
- Unable to create OpenGL context >= 3.0 ... virgl could not be initialized: 22
    - わからん
- whpx
    - "\-accel whpx,kernel-irqchip=off" まで書く
    - 理由は知らん
    - https://lists.nongnu.org/archive/html/qemu-devel/2020-12/msg00349.html

# link

- https://adam.kruszewski.name/2024-03-03-QEmu-on-windows-with-OpenGL.html
    - ほとんどこれ
    - Thank you Adam Kruszewsk
- https://gihyo.jp/admin/serial/01/ubuntu-recipe/0592
    - 技術評論社
- okuoku
    - https://zenn.dev/okuoku/articles/227043abe241a8
    - https://zenn.dev/okuoku/scraps/067a70d6cda031
    - https://zenn.dev/okuoku/scraps/4706421bafb644
    - この人を追って始めた
    - Thank you okuoku
- https://patchwork.kernel.org/project/xen-devel/patch/20230831093252.2461282-13-ray.huang@amd.com/#25493812
    - qemu のパッチのコメント
    - 実際ここでよく失敗したのでありがたい
- https://github.com/RceNinja/notes/blob/master/notes/build_qemu_with_enabled_hyper-v_acceleration_%28whpx%29_on_windows.md
    - whpx を有効化するためのビルド方法
    - 最新版だと多分組み込まれてるので必要ない