# This is a header only package
%global debug_package %{nil}

%global commit 6929bd4d25831c12d6ccb8310d96401fa3a1dc0f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20130216
%global gittag %{commitdate}git%{shortcommit}

Name:		mizuiro
Version:	0.1
Release:	1%{?dist}.%{gittag}
Summary:	A generic image C++ library

Group:		Development/Libraries
License:	Boost
URL:		https://github.com/freundlich/mizuiro
Source0:	https://github.com/freundlich/mizuiro/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:  noarch

%description
A replacement for boost::gil, but far superior. It's a library to define color
formats, convert between them as well as for creating color images and applying
generic algorithms to them.

%package devel
BuildArch:      noarch
Summary:	    A generic image C++ library
BuildRequires:	fcppt-devel
Requires:	    fcppt-devel
Requires:	    boost-devel

%description devel
A replacement for boost::gil, but far superior. It's a library to define color
formats, convert between them as well as for creating color images and applying
generic algorithms to them.

%prep
%setup -qn %{name}-%{commit}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
    -D INSTALL_LIBRARY_DIR:STRING=%{_libdir} \
    -D INSTALL_LIBRARY_DIR_BASE:STRING=%{_datadir} \
    -D INSTALL_INCLUDE_DIR:STRING=%{_includedir} \
    -D ENABLE_DOC:BOOL=OFF \
    -D ENABLE_FCPPT:BOOL=ON \
    -D ENABLE_EXAMPLES:BOOL=OFF \
    ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}


%files devel
%doc LICENSE_1_0.txt
%{_includedir}/mizuiro
%{_libdir}/cmake/mizuiro/mizuiro-config.cmake


%changelog
* Sat Feb 16 2013 Vinzenz Feenstra <vfeenstr@redhat.com> - 0.1-1.20130216git6929bd4
- Initial package
