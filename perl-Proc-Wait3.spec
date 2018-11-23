#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Proc-Wait3
Version  : 0.05
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/C/CT/CTILMES/Proc-Wait3-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CT/CTILMES/Proc-Wait3-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libproc-wait3-perl/libproc-wait3-perl_0.05-1.debian.tar.xz
Summary  : Perl extension for wait3 system call
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Proc-Wait3-lib = %{version}-%{release}
Requires: perl-Proc-Wait3-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Proc::Wait3 version 0.05
========================
Proc::Wait3 is a simple perl wrapper around the wait3(1) system call.
It reaps dead children like wait(), but also reports on the resource
usage of the child.

%package dev
Summary: dev components for the perl-Proc-Wait3 package.
Group: Development
Requires: perl-Proc-Wait3-lib = %{version}-%{release}
Provides: perl-Proc-Wait3-devel = %{version}-%{release}

%description dev
dev components for the perl-Proc-Wait3 package.


%package lib
Summary: lib components for the perl-Proc-Wait3 package.
Group: Libraries
Requires: perl-Proc-Wait3-license = %{version}-%{release}

%description lib
lib components for the perl-Proc-Wait3 package.


%package license
Summary: license components for the perl-Proc-Wait3 package.
Group: Default

%description license
license components for the perl-Proc-Wait3 package.


%prep
%setup -q -n Proc-Wait3-0.05
cd ..
%setup -q -T -D -n Proc-Wait3-0.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Proc-Wait3-0.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Proc-Wait3
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Proc-Wait3/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/Proc/Wait3.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Proc::Wait3.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/Proc/Wait3/Wait3.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Proc-Wait3/LICENSE
