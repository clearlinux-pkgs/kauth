#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kauth
Version  : 5.101.0
Release  : 59
URL      : https://download.kde.org/stable/frameworks/5.101/kauth-5.101.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.101/kauth-5.101.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.101/kauth-5.101.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: kauth-data = %{version}-%{release}
Requires: kauth-lib = %{version}-%{release}
Requires: kauth-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcoreaddons-dev
BuildRequires : polkit-qt-dev

%description
# KAuth
Execute actions as privileged user
## Introduction
KAuth provides a convenient, system-integrated way to offload actions that need
to be performed as a privileged user (root, for example) to small (hopefully
secure) helper utilities.

%package data
Summary: data components for the kauth package.
Group: Data

%description data
data components for the kauth package.


%package dev
Summary: dev components for the kauth package.
Group: Development
Requires: kauth-lib = %{version}-%{release}
Requires: kauth-data = %{version}-%{release}
Provides: kauth-devel = %{version}-%{release}
Requires: kauth = %{version}-%{release}

%description dev
dev components for the kauth package.


%package lib
Summary: lib components for the kauth package.
Group: Libraries
Requires: kauth-data = %{version}-%{release}
Requires: kauth-license = %{version}-%{release}

%description lib
lib components for the kauth package.


%package license
Summary: license components for the kauth package.
Group: Default

%description license
license components for the kauth package.


%prep
%setup -q -n kauth-5.101.0
cd %{_builddir}/kauth-5.101.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671047450
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1671047450
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kauth
cp %{_builddir}/kauth-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kauth/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kauth-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kauth/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kauth-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kauth/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kauth-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kauth/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
pushd clr-build
%make_install
popd
## install_append content
#mv %{buildroot}/etc/dbus-1/* %{buildroot}/usr/share/dbus-1/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kauth-policy-gen

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/org.kde.kf5auth.conf
/usr/share/kf5/kauth/dbus_policy.stub
/usr/share/kf5/kauth/dbus_service.stub
/usr/share/locale/af/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kauth5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kauth5_qt.qm
/usr/share/qlogging-categories5/kauth.categories
/usr/share/qlogging-categories5/kauth.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KAuth/KAuth
/usr/include/KF5/KAuth/KAuthAction
/usr/include/KF5/KAuth/KAuthActionReply
/usr/include/KF5/KAuth/KAuthExecuteJob
/usr/include/KF5/KAuth/KAuthHelperSupport
/usr/include/KF5/KAuth/KAuthObjectDecorator
/usr/include/KF5/KAuth/kauth.h
/usr/include/KF5/KAuth/kauth_version.h
/usr/include/KF5/KAuth/kauthaction.h
/usr/include/KF5/KAuth/kauthactionreply.h
/usr/include/KF5/KAuth/kauthexecutejob.h
/usr/include/KF5/KAuth/kauthhelpersupport.h
/usr/include/KF5/KAuth/kauthobjectdecorator.h
/usr/include/KF5/KAuthCore/KAuth/Action
/usr/include/KF5/KAuthCore/KAuth/ActionReply
/usr/include/KF5/KAuthCore/KAuth/ExecuteJob
/usr/include/KF5/KAuthCore/KAuth/HelperSupport
/usr/include/KF5/KAuthCore/kauth/action.h
/usr/include/KF5/KAuthCore/kauth/actionreply.h
/usr/include/KF5/KAuthCore/kauth/executejob.h
/usr/include/KF5/KAuthCore/kauth/helpersupport.h
/usr/include/KF5/KAuthCore/kauth/kauthcore_export.h
/usr/include/KF5/KAuthWidgets/KAuth/ObjectDecorator
/usr/include/KF5/KAuthWidgets/kauth/kauth_export.h
/usr/include/KF5/KAuthWidgets/kauth/objectdecorator.h
/usr/lib64/cmake/KF5Auth/KF5AuthConfig.cmake
/usr/lib64/cmake/KF5Auth/KF5AuthConfigVersion.cmake
/usr/lib64/cmake/KF5Auth/KF5AuthMacros.cmake
/usr/lib64/cmake/KF5Auth/KF5AuthTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Auth/KF5AuthTargets.cmake
/usr/lib64/cmake/KF5Auth/KF5AuthToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Auth/KF5AuthToolsTargets.cmake
/usr/lib64/libKF5Auth.so
/usr/lib64/libKF5AuthCore.so
/usr/lib64/qt5/mkspecs/modules/qt_KAuth.pri
/usr/lib64/qt5/mkspecs/modules/qt_KAuthCore.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Auth.so.5
/usr/lib64/libKF5Auth.so.5.101.0
/usr/lib64/libKF5AuthCore.so.5
/usr/lib64/libKF5AuthCore.so.5.101.0
/usr/lib64/qt5/plugins/kauth/backend/kauth_backend_plugin.so
/usr/lib64/qt5/plugins/kauth/helper/kauth_helper_plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kauth/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kauth/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kauth/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kauth/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
