
%define realname   Perl-MinimumVersion
%define version    1.20
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Find a minimum required version of perl for Perl code
Source:     http://www.cpan.org/modules/by-module/Perl/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
'Perl::MinimumVersion' takes Perl source code and calculates the minimum
version of perl required to be able to run it. Because it is based on the
PPI manpage, it can do this without having to actually load the code.

Currently it tests both the syntax of your code, and the use of explicit
version dependencies such as 'require 5.005'.

Future plans are to also add support for tracing module dependencies.

%prep
%setup -q -n %{realname}-%{version} 

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

