# opengl

khronos.org の記事

# downloads

https://www.khronos.org/opengl/wiki/Getting_Started#Downloading_OpenGL

Graphics on Linux is almost exclusively implemented using the X Window system. Supporting OpenGL on Linux involves using GLX extensions to the X Server. There is a standard Application Binary Interface defined for OpenGL on Linux that gives application compatibility for OpenGL for a range of drivers. In addition the Direct Rendering Infrastructure (DRI) is a driver framework that allows drivers to be written and interoperate within a standard framework to easily support hardware acceleration, the DRI is included in of XFree86 4.0 but may need a card specific driver to be configured after installation. These days, XFree86 has been rejected in favor of XOrg due to the change in the license of XFree86, so many developers left Xfree86 and joined the XOrg group. Popular Linux distros come with XOrg now.

Vendors have different approaches to drivers on Linux, some support Open Source efforts using the DRI, and others support closed source frameworks but all methods support the standard ABI that will allow correctly written OpenGL applications to run on Linux.

Linux 上のグラフィックスは、ほぼ独占的に X Window システムを使用して実装されます。 Linux で OpenGL をサポートするには、X サーバーに対する GLX 拡張機能を使用する必要があります。 Linux 上の OpenGL 用に定義された標準アプリケーション バイナリ インターフェイスがあり、これにより、さまざまなドライバーに対して OpenGL とアプリケーションの互換性が得られます。さらに、ダイレクト レンダリング インフラストラクチャ (DRI) は、ハードウェア アクセラレーションを簡単にサポートするために、標準フレームワーク内でドライバを記述して相互運用できるようにするドライバ フレームワークです。DRI は XFree86 4.0 に含まれていますが、後でカード固有のドライバを設定する必要がある場合があります。インストール。最近では、XFree86 のライセンス変更により XFree86 が拒否され、XOrg が使用されるようになったため、多くの開発者が Xfree86 を離れ XOrg グループに参加しました。現在、人気のある Linux ディストリビューションには XOrg が付属しています。

ベンダーは Linux 上のドライバーに対してさまざまなアプローチを持っており、DRI を使用したオープン ソースの取り組みをサポートするベンダーもあれば、クローズド ソース フレームワークをサポートするベンダーもありますが、すべてのメソッドが、正しく作成された OpenGL アプリケーションを Linux 上で実行できるようにする標準 ABI をサポートしています。

# platform specifics: linux

https://www.khronos.org/opengl/wiki/Platform_specifics:_Linux