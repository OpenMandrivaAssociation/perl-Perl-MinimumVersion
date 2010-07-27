%define upstream_name    Perl-MinimumVersion
%define upstream_version 1.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Find a minimum required version of perl for Perl code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Find::Rule::Perl)
BuildRequires: perl(PPI)
BuildRequires: perl(Perl::Critic::Utils)
BuildRequires: perl(Test::Script)
BuildRequires: perl(version) >= 0.76

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/perlver
/usr/share/man/man1/perlver.1.lzma
