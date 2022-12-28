#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-click_help_colors
Version  : 0.9.1
Release  : 13
URL      : https://files.pythonhosted.org/packages/6c/c1/abc07420cfdc046c1005e16bc8090bc1f226d631b2bd172e5a8f5524c127/click-help-colors-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/c1/abc07420cfdc046c1005e16bc8090bc1f226d631b2bd172e5a8f5524c127/click-help-colors-0.9.1.tar.gz
Summary  : Colorization of help messages in Click
Group    : Development/Tools
License  : MIT
Requires: pypi-click_help_colors-license = %{version}-%{release}
Requires: pypi-click_help_colors-python = %{version}-%{release}
Requires: pypi-click_help_colors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=================
click-help-colors
=================
|build| |pypi| |downloads|

%package license
Summary: license components for the pypi-click_help_colors package.
Group: Default

%description license
license components for the pypi-click_help_colors package.


%package python
Summary: python components for the pypi-click_help_colors package.
Group: Default
Requires: pypi-click_help_colors-python3 = %{version}-%{release}

%description python
python components for the pypi-click_help_colors package.


%package python3
Summary: python3 components for the pypi-click_help_colors package.
Group: Default
Requires: python3-core
Provides: pypi(click_help_colors)
Requires: pypi(click)

%description python3
python3 components for the pypi-click_help_colors package.


%prep
%setup -q -n click-help-colors-0.9.1
cd %{_builddir}/click-help-colors-0.9.1
pushd ..
cp -a click-help-colors-0.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672263404
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-click_help_colors
cp %{_builddir}/click-help-colors-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-click_help_colors/946bd6303d317f6d8fc6319c02f8f25434e9046f || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-click_help_colors/946bd6303d317f6d8fc6319c02f8f25434e9046f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
