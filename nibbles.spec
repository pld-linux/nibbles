Summary:	NCurses based nibbles game
Summary(pl):	Gra "nibbles" wykorzystuj±ca biblioteki NCurses
Name:		nibbles
Version:	0.0.4
Release:	5
License:	GPL
Vendor:		Project Purple ( http://www.earth.li/projectpurple/ )
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	http://www.earth.li/projectpurple/files/%{name}-v%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-window.patch
Patch2:		%{name}-score.patch
URL:		http://www.earth.li/projectpurple/progs/nibbles.html
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nibbles is a remake of the classic Snake/Nibbles game in ncurses. I am
sure that better nibbles games exist, but I thought that I'd write an
ncurses one to learn how.

%description -l pl
Nibbles jest "od¶wie¿on±" wersj± klasycznej gry w Wê¿a/Nibbles. Jestem
pewien, ¿e istnieje lepsza taka gra, ale pomy¶la³em, ¿e napiszê co¶ w
ncurses ¿eby siê nauczyæ jak to siê robi.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" DATADIR=%{_datadir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games,/var/games}

install nibbles $RPM_BUILD_ROOT%{_bindir}
touch $RPM_BUILD_ROOT/var/games/nibbles.score
cp -a nibbles.levels $RPM_BUILD_ROOT%{_datadir}/games

gzip -9nf README TODO HISTORY CREDITS example.nibblerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/nibbles
%attr(664,root,games) /var/games/nibbles.score
%{_datadir}/games/nibbles.levels
%doc *.gz
