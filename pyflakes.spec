Name:		pyflakes
Version:	0.4.0
Release:	%mkrel 2
Summary:	Simple program which checks Python source files for errors
License:	BSD
Group:      Development/Python
URL:		http://divmod.org/trac/wiki/DivmodPyflakes
Source:		%{name}/%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires:	python-devel
BuildArch:      noarch
%description
Pyflakes is a simple program which checks Python source files for errors. It is
similar to PyChecker in scope, but differs in that it does not execute the
modules to check them. This is both safer and faster, although it does not
perform as many checks.
Unlike PyLint, Pyflakes checks only for logical errors in programs; it does
not perform any checks on style.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root %buildroot

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info


%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 592427
- rebuild for python 2.7

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 500603
- update to 0.4.0
- new url

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-2mdv2010.0
+ Revision: 441987
- rebuild

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 0.3.0-1mdv2009.1
+ Revision: 341477
- New upstream release

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.2.1-3mdv2009.1
+ Revision: 325950
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.2.1-2mdv2009.0
+ Revision: 166725
- fix description-line-too-long

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2.1-2mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 12 2006 Michael Scherer <misc@mandriva.org> 0.2.1-2mdv2007.0
+ Revision: 95747
- rebuild for python 2.5
- Import pyflakes

