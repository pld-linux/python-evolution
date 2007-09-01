# TODO: rename to python-evolution
Summary:	Python bindings for Evolution
Summary(pl.UTF-8):	Wiązania Pythona do Evolution
Name:		evolution-python
Version:	0.0.3
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://files.conduit-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0ef1afcc79ae9f190ed2260eb1b1fcdd
Patch0:		%{name}-pyc.patch
URL:		http://www.conduit-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-devel
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Evolution.

%description -l pl.UTF-8

%package devel
Summary:	Development files for evolution-python binding
Summary(pl):	Pliki programistyczne wiązania evolution-python
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for evolution-python binding.

%description devel -l pl
Pliki programistyczne wiązania evolution-python.

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

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/evolution
%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/evolution/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{py_sitedir}/gtk-2.0/evolution
%{py_sitedir}/gtk-2.0/evolution/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/evolution/ebook.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/evolution/ecal.so

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/evolution-python
%dir %{_datadir}/evolution-python/defs
%{_datadir}/evolution-python/defs/ebook.defs
%{_pkgconfigdir}/evolution-python.pc
