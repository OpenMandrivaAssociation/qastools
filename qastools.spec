Summary:	A collection of desktop applications for ALSA
Name:		qastools
Version:	0.23.0
Release:	3
License:	GPLv3
Group:		Sound
Url:		http://xwmw.org/qastools
Source0:	http://sourceforge.net/projects/qastools/files/%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:	cmake ninja
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Network) cmake(Qt5Svg) cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(alsa)

%description
%{summary}

Features:
   * Desktop ALSA mixer applications
   * Desktop ALSA configuration browser

%prep
%setup -qn %{name}-v%{version}

%build
%cmake_qt5 -G Ninja
%ninja

%install
%ninja_install -C build

# make the .desktop file compliant with freedesktop specs
for i in qasconfig qashctl qasmixer;
do
desktop-file-install \
	--add-category="X-OpenMandrivaLinux-Sound" \
	%{buildroot}%{_datadir}/applications/$i.desktop

desktop-file-validate %{buildroot}%{_datadir}/applications/$i.desktop
done

# it'll be %%doc'ed
rm -f %{buildroot}%{_datadir}/%{name}/COPYING

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
