%global commit 1486f95d09d979ce4118e20a3dcb14d42bf67df2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20130216
%global gittag %{commitdate}git%{shortcommit}

Name:	    libawl
Version:    0.1
Release:	1%{?dist}.%{gittag}
Summary:	Abstract Window Library

Group:		Development/Libraries
License:	Boost
URL:		https://github.com/pmiddend/libawl
Source0:	https://github.com/pmiddend/libawl/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:	fcppt-devel
Requires:	    fcppt

%description
The Abstract Window Library is a C++ library providing an abstract interface
for managing of windows and events of different platforms.

%package devel
Summary:    Development files for the Abstract Window Library
Requires:   boost-devel
Requires:   fcppt-devel
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for the Abstract Window Library

# %package doc
# Summary:    Documentation for the Abstract Window Library
# BuildArch:  noarch
# BuildRequires:   doxygen
#
# %description doc
# Documentation for the Abstract Window Library

%prep
%setup -qn %{name}-%{commit}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
    -D INSTALL_LIBRARY_DIR:STRING=%{_libdir} \
    -D INSTALL_LIBRARY_DIR_BASE:STRING=%{_datadir} \
    -D INSTALL_INCLUDE_DIR:STRING=%{_includedir} \
    -D ENABLE_EXAMPLES:BOOL=OFF \
    -D AWL_SO_VERSION:STRING=%{version} \
    ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

#%check
#pushd %{_target_platform}
#ctest
#popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%doc
%{_includedir}/awl
%{_libdir}/cmake/awl
%{_datadir}/cmake/Modules/AwlMainGenerator.cmake
%{_libdir}/libawl.so

%files
%doc
%{_libdir}/libawl.so.%{version}


%changelog
* Sat Feb 16 2013 Vinzenz Feenstra <vfeenstr@redhat.com> - 0.1-1.20130216git1486f95
- Initial package

