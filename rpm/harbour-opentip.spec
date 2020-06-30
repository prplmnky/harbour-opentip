# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-opentip

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libapplicationsettings|libcore|liblanguage.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    OpenTip
Version:    2.0
Release:    0
Group:      Qt/Qt
License:    GPLv3
URL:        https://github.com/prplmnky/harbour-opentip
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-opentip.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Open Source Tip Calculator


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%attr(755, root, root) %{_bindir}/%{name}
%attr(755, root, root) %{_datadir}/%{name}
%attr(644, root, root) %{_datadir}/%{name}/qml/*.qml
%attr(644, root, root) %{_datadir}/%{name}/qml/cover/*.qml
%attr(644, root, root) %{_datadir}/%{name}/qml/pages/*.qml
%attr(644, root, root) %{_datadir}/%{name}/translations/*.qm
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/QmlLogger/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/OpenTip/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/Components/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/Database/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/FileManagement/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/JS/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/Language/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/Settings/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/Utilities/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/opentip/SailfishWidgets/*.qmltypes
%attr(644, root, root) %{_datadir}/applications/%{name}.desktop
%attr(644, root, root) %{_datadir}/icons/hicolor/86x86/apps/%{name}.png
# >> files
# << files
