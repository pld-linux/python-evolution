#
Summary:	Python bindings for Evolution
Name:		evolution-python
Version:	0.0.3
Release:	1
License:	GPLv2
Group:		Development/Libraries
Source0:	http://files.conduit-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0ef1afcc79ae9f190ed2260eb1b1fcdd
Patch0:		%{name}-pyc.patch
URL:		http://www.conduit-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-devel
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Evolution.

%package devel
Summary:	Header files for evolution-python library
Summary(pl):	Pliki nag³ówkowe biblioteki evolution-python
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for evolution-python library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki evolution-python.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/evolution/
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{py_sitedir}/gtk-2.0/evolution/__init__.py[co]
%dir %{py_sitedir}/gtk-2.0/evolution
%attr(755,root,root) %{py_sitedir}/gtk-2.0/evolution/ebook.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/evolution/ecal.so
%dir %{_datadir}/evolution-python
%dir %{_datadir}/evolution-python/defs
%{_datadir}/evolution-python/defs/ebook.defs

%files devel
%{_pkgconfigdir}/evolution-python.pc
%{py_sitedir}/gtk-2.0/evolution/ebook.la
%{py_sitedir}/gtk-2.0/evolution/ecal.la
