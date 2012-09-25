Name:        vsqlite++
Version:    0.3.7
Release:    2%{?dist}
Summary:    Well designed C++ sqlite 3.x wrapper library

Group:      Development/Libraries
License:    BSD
URL:        https://github.com/vinzenz/vsqlite--
Source0:    https://github.com/downloads/vinzenz/vsqlite--/%{name}-%{version}.tar.gz

BuildRequires: premake, boost-devel, sqlite-devel, autoconf, automake, libtool

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package static
Summary:        Static library for %{name}
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
This package contains the static version of libvsqlitepp for %{name}.

%prep
%setup -q
./autogen.sh

%build
%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}

%install
# static
install -p -m 755 -d %{buildroot}%{_libdir}
install -p -m 755 -d %{buildroot}%{_libdir}
install -p -m 755 -d %{buildroot}%{_includedir}/sqlite
install -m 644 include/sqlite/*.hpp %{buildroot}%{_includedir}/sqlite 
# base
install -p -m 755 -d %{buildroot}%{_libdir}
make DESTDIR=%{buildroot} install

# and lets get rid of .la 
rm -f %{buildroot}%{_libdir}/libvsqlitepp.la

%post devel -p /sbin/ldconfig 
%post -p /sbin/ldconfig 
%postun devel -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files static
%{_libdir}/libvsqlitepp.a

%files devel
%doc examples/sqlite_wrapper.cpp
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite

%files
%doc Changelog README LICENSE TODO VERSION 
%{_libdir}/libvsqlitepp.so.*

%changelog
* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.7-2
- Fix for %%description spelling 'ibrary' => 'library'
- Fix for unused libm dependency
* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.7-1
- Initial package

