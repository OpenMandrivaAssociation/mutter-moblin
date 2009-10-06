Name: mutter-moblin
Summary: Moblin Netbook plugin for Metacity Clutter, aka, Mutter
Group: User Interface/Desktops
Version: 0.40.3
License: GPLv2
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/mutter-moblin/snapshot/mutter-moblin-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libstartup-notification-1-devel
BuildRequires: libmesagl-devel
BuildRequires: mutter-devel
BuildRequires: libgnome-menu-devel
BuildRequires: libnbtk-devel
BuildRequires: libjana-devel
BuildRequires: mojito-devel
BuildRequires: moblin-clutter-mozembed-devel
BuildRequires: libbickley-devel
BuildRequires: libbognor-regis-devel
BuildRequires: libanerley-devel

BuildRequires: intltool

Requires: gnome-menus
Requires: mutter
Requires: gnome-menus

%description
Moblin Netbook plugin for Metacity Clutter, aka, Mutter

%prep
%setup -q

%build
autoreconf
%configure --enable-netpanel --enable-ahoghill --enable-people --enable-debug --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang mutter-moblin  || echo -n >> mutter-moblin.lang

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -f mutter-moblin.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/metacity/plugins/clutter/*
%{_datadir}/mutter-moblin/*
