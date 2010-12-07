%define		_class		Math
%define		_subclass	Numerical
%define		_subsubclass	RootFinding
%define		upstream_name	%{_class}_%{_subclass}_%{_subsubclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	%mkrel 6
Summary:	Numerical analysis root finding methods
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Math_Numerical_RootFinding/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provide various numerical analysis methods for find root
Available Methods:
- Bisection
- False Position
- Fixed Point
- Newton-Raphson
- Secant

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/README.txt
%doc %{upstream_name}-%{version}/docs/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


