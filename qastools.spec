Name:		qastools
Version:	0.17.1
Release:	1
Summary:	A collection of desktop applications for ALSA
Url:		http://xwmw.org/qastools
Source0:	http://sourceforge.net/projects/qastools/files/0.17.1/%{name}_%{version}.tar.xz
Patch0:		%{name}-qasconfig-desktop-file.patch
Patch1:		%{name}-qashctl-desktop-file.patch
Patch2:		%{name}-qasmixer-desktop-file.patch
License:	GPLv3
Group:		Sound
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	libalsa-devel
BuildRequires:	desktop-file-utils

Obsoletes:	qasmixer <= 0.15
Conflicts:	qasmixer

%description
%{summary}

Features:
   * Desktop ALSA mixer applications
   * Desktop ALSA configuration browser


%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .qasconfigdesk
%patch1 -p1 -b .qashctldesk
%patch2 -p1 -b .qasmixerdesk

%build
%cmake
%make

%install
%makeinstall_std -C build

# make the .desktop file compliant with freedesktop specs
for i in qasconfig qashctl qasmixer;
do
desktop-file-validate %{buildroot}%{_datadir}/applications/$i.desktop
done

# it'll be %%doc'ed
rm -f %{buildroot}%{_datadir}/%{name}/COPYING

#%find_lang %{name}

%files
# -f %{name}.lang
%doc CHANGELOG COPYING README
%{_bindir}/qasconfig
%{_bindir}/qashctl
%{_bindir}/qasmixer
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_mandir}/man1/qasconfig.1.*
%{_mandir}/man1/qashctl.1.*
%{_mandir}/man1/qasmixer.1.*
%{_datadir}/%{name}/icons/*.svg
%{_datadir}/%{name}/widgets/sw_joined_*.svg
%{_datadir}/%{name}/l10n/%{name}_*.qm
