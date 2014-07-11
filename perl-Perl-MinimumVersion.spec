%define modname	Perl-MinimumVersion
%define modver 1.37

Summary:	Find a minimum required version of perl for Perl code



Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Perl::Critic::Utils)
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(version) >= 0.76
BuildRequires:	perl-devel

%description
'Perl::MinimumVersion' takes Perl source code and calculates the minimum
version of perl required to be able to run it. Because it is based on the
PPI manpage, it can do this without having to actually load the code.

Currently it tests both the syntax of your code, and the use of explicit
version dependencies such as 'require 5.005'.

Future plans are to also add support for tracing module dependencies.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_bindir}/perlver
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*





