#
# Conditional build:
%bcond_with	tests	# unit tests

%define		pdir	Devel
%define		pnam	Caller
Summary:	Devel::Caller - meatier versions of Perl function "caller"
Summary(pl.UTF-8):	Devel::Caller - treściwsza wersja perlowej funkcji "caller"
Name:		perl-Devel-Caller
Version:	2.06
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af52f47979b3c9358af9e5d8c283f263
URL:		https://metacpan.org/dist/Devel-Caller
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-PadWalker >= 0.08
BuildRequires:	perl-Test-Simple
%endif
Requires:	perl-PadWalker >= 0.08
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Caller Perl module provides meatier versions of "caller"
function.

%description -l pl.UTF-8
Moduł Perla Devel::Caller udostępnia treściwszą wersję funkcji
"caller".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Devel/Caller.pm
%dir %{perl_vendorarch}/auto/Devel/Caller
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Caller/Caller.so
%{_mandir}/man3/Devel::Caller.3pm*
