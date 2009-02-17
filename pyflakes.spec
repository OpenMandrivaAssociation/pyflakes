Name:		pyflakes
Version:	0.3.0
Release:	%mkrel 1
Summary:	Simple program which checks Python source files for errors
License:	BSD
Group:      Development/Python
URL:		http://divmod.org/projects/pyflakes
Source:		http://divmod.org/static/projects/%{name}/%{name}-%{version}.tar.bz2
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
