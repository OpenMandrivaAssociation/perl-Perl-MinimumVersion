%define upstream_name    Perl-MinimumVersion
%define upstream_version 1.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Find a minimum required version of perl for Perl code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Perl::Critic::Utils)
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(version) >= 0.76
BuildRequires:	perl-devel

BuildArch:	noarch

%description
'Perl::MinimumVersion' takes Perl source code and calculates the minimum
version of perl required to be able to run it. Because it is based on the
PPI manpage, it can do this without having to actually load the code.

Currently it tests both the syntax of your code, and the use of explicit
version dependencies such as 'require 5.005'.

Future plans are to also add support for tracing module dependencies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/perlver


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.280.0-4mdv2012.0
+ Revision: 765593
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.280.0-2
+ Revision: 676637
- rebuild

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.280.0-1
+ Revision: 672858
- update to new version 1.28

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.260.0-2
+ Revision: 655426
- update file list
- rebuild for updated spec-helper

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2011.0
+ Revision: 561040
- update to 1.26

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2011.0
+ Revision: 552581
- update to 1.25

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.1
+ Revision: 494935
- update to 1.24

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.220.0-1mdv2010.1
+ Revision: 470498
- adding missing buildrequires:
- update to 1.22

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.0
+ Revision: 401616
- rebuild using %%perl_convert_version
- fixed license field

* Sat May 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20-1mdv2010.0
+ Revision: 373720
- another round of buildrequires
- yet another missing buildrequires
- adding missing buildrequires
- import perl-Perl-MinimumVersion


* Fri May 08 2009 cpan2dist 1.20-1mdv
- initial mdv release, generated with cpan2dist

