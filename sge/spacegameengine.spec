%global commit c1337075488ab1e81b04cebe8584b80de3441992
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20130216
%global gittag %{commitdate}git%{shortcommit}

Name:		spacegameengine
Version:	0.1
Release:	1%{?dist}.%{gittag}
Summary:	An easy to use game engine written in C++

Group:		Development/Libraries
License:	LGPLv2+
URL:		https://github.com/freundlich/spacegameengine
Source0:	https://github.com/freundlich/spacegameengine/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:	fcppt-devel
BuildRequires:	libawl-devel
BuildRequires:	mizuiro-devel
BuildRequires:	boost-devel
BuildRequires:	cmake

%description
sge, which is short for spacegameengine, is a multimedia engine written in
C++.
It uses clean and modern C++, which employs RAII, especially smart pointers,
optionals, strong tyepedefs, interfaces for abstraction and template meta
configuration.
sge is modular, which means each functionality is available either through a
fundamental library like renderer, input, etc. or through a support library
like camera, shader, etc.
The back-ends are abstracted as plugins where this makes sense, for example
D3D9, OpenGL, Direct Input and X11 Input.

%prep
%setup -qn %{name}-%{commit}

%package devel
Summary:    The development files for the spacegameengine
Requires: %{name} = %{version}-%{release}

%description devel
The development files for the spacegameengine.
sge, which is short for spacegameengine, is a multimedia engine written in
C++.
It uses clean and modern C++, which employs RAII, especially smart pointers,
optionals, strong tyepedefs, interfaces for abstraction and template meta
configuration.
sge is modular, which means each functionality is available either through a
fundamental library like renderer, input, etc. or through a support library
like camera, shader, etc.

%package media
Summary:    The media files for the spacegameengine
Requires: %{name} = %{version}-%{release}

%description media
Media files for the spacegameengine.

%package plugin-devil
Summary:    The DevIL plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: DevIL-devel

%description plugin-devil
This package contains the DevIL back-end for the spacegameengine.

%package plugin-evdev
Summary:    The event device plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}

%description plugin-evdev
This package contains the evdev back-end for the spacegameengine.

%package plugin-libpng
Summary:    The libpng plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: libpng-devel

%description plugin-libpng
This package contains the libpng back-end for the spacegameengine.

%package plugin-openal
Summary:    The openAL plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: openal-soft-devel

%description plugin-openal
This package contains the OpenAL back-end for the spacegameengine.

%package plugin-opengl
Summary:    The OpenGL plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: glew-devel
BuildRequires: mesa-libGL-devel

%description plugin-opengl
This package contains the OpenGL back-end for the spacegameengine

%package plugin-pango
Summary:    The pango plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: pango-devel

%description plugin-pango
This package contains the pango back-end for the spacegameengine.

%package plugin-vorbis
Summary:    The vorbis plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: libvorbis-devel

%description plugin-vorbis
This package contains the vorbis back-end for the spacegameengine.

%package plugin-wave
Summary:    The wave sound plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}

%description plugin-wave
This package contains the wave back-end for the spacegameengine.

%package plugin-x11input
Summary:    The X11 input plugin for the spacegameengine
Requires: %{name} = %{version}-%{release}
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXext-devel

%description plugin-x11input
This package contains the X11 Input back-end for the spacegameengine.

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
    -D INSTALL_LIBRARY_DIR:STRING=%{_libdir} \
    -D INSTALL_LIBRARY_DIR_BASE:STRING=%{_datadir} \
    -D INSTALL_INCLUDE_DIR:STRING=%{_includedir} \
    -D ENABLE_TEST:BOOL=ON \
    -D ENABLE_RENDEREROPENGL:BOOL=ON \
    -D ENABLE_SCENIC:BOOL=OFF \
    -D ENABLE_CG:BOOL=OFF \
    -D ENABLE_OPENCL:BOOL=OFF \
    -D ENABLE_OPENGL:BOOL=ON \
    -D ENABLE_OPENAL:BOOL=ON \
    -D ENABLE_POSTPROCESSING:BOOL=OFF \
    -D ENABLE_DEVIL:BOOL=ON \
    -D ENABLE_SHADER:BOOL=OFF \
    -D ENABLE_EXAMPLES:BOOL=OFF \
    -D SGE_SO_VERSION:STRING=%{version} \
    ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc
%{_bindir}/sge_tool_control_config
%{_libdir}/libsge*.so.*
%{_libdir}/sge

%files media
%{_datadir}/sge/media

%files plugin-devil
%{_libdir}/sge/libsgedevil.so

%files plugin-evdev
%{_libdir}/sge/libsgeevdev.so

%files plugin-libpng
%{_libdir}/sge/libsgelibpng.so

%files plugin-openal
%{_libdir}/sge/libsgeopenal.so

%files plugin-opengl
%{_libdir}/sge/libsgeopengl.so

%files plugin-pango
%{_libdir}/sge/libsgepango.so

%files plugin-vorbis
%{_libdir}/sge/libsgevorbis.so

%files plugin-wave
%{_libdir}/sge/libsgewave.so

%files plugin-x11input
%{_libdir}/sge/libsgex11input.so

%files devel
%doc
%{_includedir}/majutsu
%{_includedir}/sge
%{_libdir}/cmake/sge
%{_libdir}/libsge*.so
%{_datadir}/cmake/Modules/FindCEGUI.cmake
%{_datadir}/cmake/Modules/FindCg.cmake
%{_datadir}/cmake/Modules/SGECustomPath.cmake


%changelog
* Sat Feb 16 2013 Vinzenz Feenstra <vfeenstr@redhat.com> - 0.1-1.20130216gitc133707
- Initial package
