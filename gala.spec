%define		rel		1
%define		subver	293
Summary:	Pantheon's Window Manager
Name:		gala
Version:	0.1.0
Release:	0.%{subver}.%{rel}
License:	GPL v3
Group:		X11/Applications
Source0:	%{name}.tar.bz2
# Source0-md5:	09d6ff9d0425a62cfcb623276c1a0cdf
URL:		https://launchpad.net/gala
BuildRequires:	bamf3-devel
BuildRequires:	clutter-devel >= 1.9.16
BuildRequires:	clutter-gtk-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	gettext-devel
BuildRequires:	granite-devel
BuildRequires:	libgee0.6-devel
BuildRequires:	mutter-devel >= 3.4
BuildRequires:	pkgconfig
BuildRequires:	plank-devel >= 0.2.0.748
BuildRequires:	vala >= 0.16.1
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	glib2 >= 1:2.26.0
Requires:	gtk-update-icon-cache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gala is a window & compositing manager based on libmutter and designed
by elementary for use with Pantheon Shell.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%glib_compile_schemas

%postun
%update_desktop_database
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
