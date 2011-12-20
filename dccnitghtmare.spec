Summary:	3D single player RPG in a satirical post-apocalyptical world
Name:		dccnitghtmare
Version:	0.8
Release:	%mkrel 1
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
BuildRequires:	libvorbis-devel
BuildRequires:	openal-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
Requires:	%{name}-data = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%__rm -rf %{buildroot}
%makeinstall

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%__mkdir_p  %{buildroot}%{_datadir}/pixmaps
%__cp data/dnt-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files data
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*