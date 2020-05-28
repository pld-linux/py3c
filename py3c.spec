Summary:	A Python 2/3 compatibility layer for C extensions
Name:		py3c
Version:	1.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/encukou/py3c/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0-md5:	95be2e17f0541de2ba3e1b68dee4a9da
URL:		https://libbsd.freedesktop.org/
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py3c helps you port C extensions to Python 3.
 
It provides a detailed guide, and a set of macros to make porting easy
and reduce boilerplate.

%prep
%setup -q

%build
%{__make} includedir=%{_includedir} py3c.pc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_includedir},%{_pkgconfigdir}}

cp -p include/py3c.h $RPM_BUILD_ROOT%{_includedir}
cp -pr include/py3c $RPM_BUILD_ROOT%{_includedir}
cp -p py3c.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst CONTRIBUTING README.rst
%{_includedir}/py3c.h
%dir %{_includedir}/py3c
%{_includedir}/py3c/*.h
%{_pkgconfigdir}/py3c.pc
