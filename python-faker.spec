%global pkgname faker
%global sum Faker is a Python package that generates fake data for you
%global desc Faker is a Python package that generates fake data for you. Whether you need \
to bootstrap your database, create good-looking XML documents, fill-in your \
persistence to stress test it, or anonymize data taken from a production \
service, Faker is for you.

Name:           python-%{pkgname}
Version:        0.5.9
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://www.joke2k.net/faker/
Source:         https://github.com/joke2k/%{pkgname}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel 
BuildRequires:  python3-devel
BuildRequires:  python-sphinx
BuildRequires:  python-dateutil
BuildRequires:  python-ipaddress

%description
%{desc}

%package -n python2-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pkgname}}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python2-%{pkgname}
%{desc}

%package -n python3-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pkgname}}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python3-%{pkgname}
%{desc}

%package doc
Summary:        Documentation for python-%{pkgname}

%description doc
Documentation for python-%{pkgname}

%prep
%autosetup -n %{pkgname}-%{version}

%build
%py2_build
%py3_build
pushd docs
PYTHONPATH='..' %make_build html
PYTHONPATH='..' %make_build man
find . -type f -name '.buildinfo' -delete
popd

%install
%py2_install
%py3_install
install -D -m 0644 docs/_build/man/faker.1 %{buildroot}%{_mandir}/man1/faker.1

# Tests fail to run:
# https://github.com/joke2k/faker/issues/292
#%%check
#%%{__python2} setup.py test
#%%{__python3} setup.py test

%files -n python2-%{pkgname}
%license LICENSE.txt
%{python2_sitelib}/%{pkgname}
%{python2_sitelib}/fake_factory-%{version}-py*.egg-info

%files -n python3-%{pkgname}
%license LICENSE.txt
%{_bindir}/faker
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/fake_factory-%{version}-py*.egg-info
%{_mandir}/man1/faker.1*

%files doc
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst docs/_build/html

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.9-1
- Version 0.5.9

* Mon Jul 04 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.8-1
- Version 0.5.8

* Sun Mar 13 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.7-1
- Version 0.5.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.3-7
- Leave only python3 version of faker script

* Wed Nov 25 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.3-6
- link binary for different python versions

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 03 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.3-4
- Move all doc files to the doc subpackage
- Include the man page in the main packages

* Fri Oct 30 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.3-3
- Add documentation

* Thu Oct 29 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.3-2
- Add python provides and follow naming guidelines
- Rename faker binary

* Fri Oct 23 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.3-1
- Initial package
