Summary:	NCurses based nibbles game.
Summary(pl):	Gra "nibbles" wykorzystuj±ca biblioteki NCurses
Name:		nibbles
Version:	0.0.4
Release:	1
License:	GPL
Vendor:		Project Purple ( http://www.earth.li/projectpurple/ )
Group:		Games
Group(pl):	Gry
Source0:	http://www.earth.li/projectpurple/files/%{name}-v%{version}.tar.gz
Patch0:		nibbles-Makefile.patch
Patch1:		nibbles-window.patch
BuildRequires:	ncurses-devel >= 5.0
Requires:	ncurses >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nibbles is a remake of the classic Snake/Nibbles game in ncurses. I am sure
that better nibbles games exist, but I thought that I'd write an ncurses
one to learn how.

%description -l pl
Nibbles jest "od¶wie¿on±" wersj± klasycznej gry w Wê¿a/Nibbles. Jestem pewien,
¿e istnieje lepsza taka gra, ale pomy¶la³em, ¿e napiszê co¶ w ncurses ¿eby
siê nauczyæ jak to siê robi

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" DATADIR=%{_datadir}

%install
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_datadir}/games,/var/lib/games}
install nibbles $RPM_BUILD_ROOT%{_prefix}/games
touch $RPM_BUILD_ROOT/var/lib/games/nibbles.score
cp -a nibbles.levels $RPM_BUILD_ROOT/usr/share/games

gzip -9nf README TODO HISTORY CREDITS example.nibblerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_prefix}/games/nibbles
%attr(664,root,games) /var/lib/games/nibbles.score
%{_datadir}/games/nibbles.levels
%doc *.gz
