%define panel_name	moblin-panel
%define panel_major	0
%define panel_libname	%mklibname %{panel_name} %{panel_major}
%define panel_develname	%mklibname %{panel_name} -d

Name: mutter-moblin
Summary: Moblin Netbook plugin for Metacity Clutter, aka, Mutter
Group: Graphical desktop/Other 
Version: 0.43.2
License: GPLv2
URL: http://www.moblin.org
Release: %mkrel 4
Source0: http://git.moblin.org/cgit.cgi/mutter-moblin/snapshot/mutter-moblin-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: startup-notification-devel
BuildRequires: libmesagl-devel
BuildRequires: moblin-mutter-devel
BuildRequires: libgnome-menu-devel
BuildRequires: nbtk-devel
BuildRequires: jana-devel
BuildRequires: mojito-devel
BuildRequires: clutter-mozembed-devel
BuildRequires: bickley-devel
BuildRequires: bognor-regis-devel
BuildRequires: anerley-devel
BuildRequires: gnome-common
BuildRequires: intltool

Requires: gnome-menus
Requires: moblin-mutter
Requires: %{panel_libname} = %{version}-%{release}

%description
Moblin Netbook plugin for Metacity Clutter, aka, Mutter

%package -n %{panel_libname}
Summary: Moblin panel libraries
Group: System/Libraries

%description -n %{panel_libname}
Moblin panel libraries

%package -n %{panel_develname}
Summary: Development libraries and headers for %{panel_name}
Group: Development/C
Requires: %{panel_libname} = %{version}-%{release}
Provides: %{panel_name}-devel

%description -n %{panel_develname}
Development environment for %{panel_name}

%prep
%setup -q

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_libdir}/mutter/plugins/*
%{_datadir}/mutter-moblin/*
%{_datadir}/locale/*

%files -n %{panel_libname}
%defattr(-,root,root,-)
%{_libdir}/lib%{panel_name}.so.%{panel_major}*

%files -n %{panel_develname}
%defattr(-,root,root,-)
%dir %{_includedir}/lib%{panel_name}
%{_includedir}/lib%{panel_name}/*
%{_libdir}/lib%{panel_name}.la
%{_libdir}/lib%{panel_name}.so
%{_libdir}/pkgconfig/%{panel_name}.pc
