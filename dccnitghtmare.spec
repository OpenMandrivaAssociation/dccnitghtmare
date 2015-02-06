Summary:	3D single player RPG in a satirical post-apocalyptical world
Name:		dccnitghtmare
Version:	0.8
Release:	3
License:	GPLv3
Group:		Games/Adventure
URL:		http://dnt.dnteam.org/cgi-bin/about.py
Source:		http://sourceforge.net/projects/dccnitghtmare/files/dccnitghtmare/dccnitghtmare%20%{version}/%{name}-%{version}.tar.bz2
Source1:	dccnitghtmare.png
Patch0:		dccnitghtmare-0.8-linking.patch
# Be sure to check if it's still needed in next version
# The game should be able to save options if there is no
# .dccnitghtmare exist in user home yet
Patch1:		dccnitghtmare-0.8-options.patch
BuildRequires:	cal3d-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	SDL_ttf-devel
Requires:	%{name}-data = %{version}

%description
DccNiTghtmare is a project to make a 3d realtime RPG with battles
in turns schema. The game will have a comic, sarcastic and critic
story in a academic enviroment with a non-linear story/drama.

%package	data
Summary:	DccNiTghtmare data files (graphics, music, maps etc)
Requires:	%{name} = %{version}
Group:		Games/Adventure
BuildArch:	noarch

%description	data
Data files used to play DccNiTghtmare.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=DccNiTghtmare
Comment=3D single player RPG game
Exec=dccnitghtmare
Icon=dccnitghtmare
Terminal=false
Categories=Game;AdventureGame;
EOF

mkdir -p  %{buildroot}%{_datadir}/pixmaps
cp data/dnt-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
* Tue Dec 20 2011 Andrey Bondrov <abondrov@mandriva.org> 0.8-1mdv2011.0
+ Revision: 743945
- imported package dccnitghtmare

