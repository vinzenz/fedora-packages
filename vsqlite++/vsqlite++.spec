Name:        vsqlite++
Version:    0.3.7
Release:    2%{?dist}
Summary:    Well designed C++ sqlite 3.x wrapper library

Group:      Development/Libraries
License:    BSD
URL:        https://github.com/vinzenz/vsqlite--
Source0:    https://github.com/downloads/vinzenz/vsqlite--/%{name}-%{version}.tar.gz

BuildRequires:  premake,
                boost-devel,
                sqlite-devel,
                autoconf,
                automake,
                libtool,
                doxygen,
                graphviz

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package doc
Summary:        Development documentation for %{name}
Group:          Development/Libraries

%description doc
This package contains development documenation files for %{name}.

%prep
%setup -q
./autogen.sh

%build
%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
doxygen Doxyfile

%install
# devel & base
install -p -m 755 -d %{buildroot}%{_libdir}
# devel only
install -p -m 755 -d %{buildroot}%{_includedir}/sqlite
install -m 644 include/sqlite/*.hpp %{buildroot}%{_includedir}/sqlite
# docs
install -p -m 755 -d %{buildroot}%{_docdir}

# build for all
make DESTDIR=%{buildroot} install

# and lets get rid of .a && .la 
#rm -f %{buildroot}%{_libdir}/libvsqlitepp.(la|a)

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig

%files doc
%doc Changelog README LICENSE examples/sqlite_wrapper.cpp html/*

%files devel
%doc Changelog README LICENSE
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite
# Don't add .la/.a to the package
%exclude %{_libdir}/libvsqlitepp.la
%exclude %{_libdir}/libvsqlitepp.a

%files
%doc Changelog README LICENSE 
%{_libdir}/libvsqlitepp.so.*

%changelog
* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.7-2
- Fix for %%description spelling 'ibrary' => 'library'
- Fix for unused libm dependency
- Include Changelog, README and LICENSE to devel
- Removed TODO, VERSION
- Removed duplicated lines in the install sectin
- New doc sub package for the html documentation and code example
- Removed static package
- Removed unnecessary ldconfig call on devel package
- One BuildRequires entry per line

* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.7-1
- Initial package

