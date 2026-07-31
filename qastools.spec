Summary:	A collection of desktop applications for ALSA
Name:	qastools
Version:	1.5.0
Release:	1
License:	GPLv3+
Group:	Sound
Url:		https://gitlab.com/sebholt/qastools
Source0:	https://gitlab.com/sebholt/qastools/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:		cmake >= 3.25
BuildRequires:		desktop-file-utils
BuildRequires:		glslc
BuildRequires:		ninja
BuildRequires:		qmake-qt6
BuildRequires:		cmake(Qt6Core)
BuildRequires:		cmake(Qt6Core5Compat)
BuildRequires:		cmake(Qt6DBus)
BuildRequires:		cmake(Qt6Gui)
BuildRequires:		cmake(Qt6Network)
BuildRequires:		cmake(Qt6Svg)
BuildRequires:		cmake(Qt6Widgets)
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(glu)
BuildRequires:		pkgconfig(udev)
BuildRequires:		pkgconfig(vulkan)
BuildRequires:		pkgconfig(xkbcommon)

%description
A collection of Qt-based mixer and setup tools for ALSA.
At the moment there are three applications:
* QasMixer - A graphical mixer similiar to alsamixer.
* QasHctl - A graphical mixer for ALSA's "High level Control Interface".
* QasConfig - A viewer for ALSA's configuration tree.

%files
%doc CHANGELOG COPYING README.md
%{_bindir}/qasconfig
%{_bindir}/qashctl
%{_bindir}/qasmixer
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_mandir}/man1/qasconfig.1*
%{_mandir}/man1/qashctl.1*
%{_mandir}/man1/qasmixer.1*
%{_datadir}/%{name}/icons/*.svg
%{_datadir}/%{name}/widgets/sw_joined_*.svg
%{_datadir}/%{name}/l10n/%{name}_*.qm
%{_datadir}/metainfo/qasmixer.appdata.xml
%{_datadir}/metainfo/qasconfig.appdata.xml
%{_datadir}/metainfo/qashctl.appdata.xml

#-----------------------------------------------------------------------------
   
%prep
%autosetup -n qastools-v1.5.0 -p1


%build
%cmake -G Ninja
%ninja_build


%install
%ninja_install -C build

# It'll be %%doc'ed
rm -f %{buildroot}%{_datadir}/%{name}/COPYING
