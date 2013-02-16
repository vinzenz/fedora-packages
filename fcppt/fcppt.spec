%global commit 54f20a42722baf101f811b54ce7180b073d70a6a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20130216
%global gittag %{commitdate}git%{shortcommit}

Name: fcppt
Version:	0.12.1
Release:	1%{?dist}.%{gittag}
Summary:	Freundlich's C++ toolkit

Group:		Development/Libraries
License:	Boost
URL:	    http://fcppt.org
Source0:	https://github.com/freundlich/fcppt/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem
BuildRequires:  boost-system
Requires:	boost-filesystem

%description
Freundlich's C++ toolkit.

%package devel
Summary:    Development files for Freundlich's C++ toolkit
Requires:   boost-devel
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for Freundlich's C++ toolkit.

%package doc
Summary:    Documentation for Freundlich's C++ toolkit
BuildArch:  noarch
BuildRequires:   doxygen

%description doc
Documentation for Freundlich's C++ toolkit.

%prep
%setup -qn %{name}-%{commit}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
    -D INSTALL_LIBRARY_DIR:STRING=%{_libdir} \
    -D INSTALL_LIBRARY_DIR_BASE:STRING=%{_datadir} \
    -D INSTALL_INCLUDE_DIR:STRING=%{_includedir} \
    -D INSTALL_DOC_DIR:STRING=%{_docdir}/fcppt \
    -D ENABLE_DOC:BOOL=ON \
    -D ENABLE_EXAMPLES:BOOL=OFF \
    ..
popd

make all doc %{?_smp_mflags} -C %{_target_platform}

%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
pushd %{_target_platform}
ctest
popd

%files doc
%doc LICENSE_1_0.txt
%doc %{_docdir}/fcppt

%files devel
%doc LICENSE_1_0.txt README.markdown
%{_includedir}/fcppt
%{_libdir}/cmake/fcppt/*.cmake
%{_datadir}/cmake/Modules/*.cmake
%{_libdir}/libfcppt_core.so
%{_libdir}/libfcppt_filesystem.so

%files
%doc LICENSE_1_0.txt README.markdown
%{_libdir}/libfcppt_core.so.*
%{_libdir}/libfcppt_filesystem.so.*

%changelog
* Sat Feb 16 2013 Vinzenz Feenstra <vfeenstr@redhat.com> - 0.12.1-1.20130216git54f20a4
- Initial package

