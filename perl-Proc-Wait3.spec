#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Proc-Wait3
Version  : 0.05
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/C/CT/CTILMES/Proc-Wait3-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CT/CTILMES/Proc-Wait3-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libproc-wait3-perl/libproc-wait3-perl_0.05-1.debian.tar.xz
Summary  : Perl extension for wait3 system call
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Proc-Wait3-license = %{version}-%{release}
Requires: perl-Proc-Wait3-perl = %{version}-%{release}
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
Provides: perl-Proc-Wait3-devel = %{version}-%{release}
Requires: perl-Proc-Wait3 = %{version}-%{release}

%description dev
dev components for the perl-Proc-Wait3 package.


%package license
Summary: license components for the perl-Proc-Wait3 package.
Group: Default

%description license
license components for the perl-Proc-Wait3 package.


%package perl
Summary: perl components for the perl-Proc-Wait3 package.
Group: Default
Requires: perl-Proc-Wait3 = %{version}-%{release}

%description perl
perl components for the perl-Proc-Wait3 package.


%prep
%setup -q -n Proc-Wait3-0.05
cd %{_builddir}
tar xf %{_sourcedir}/libproc-wait3-perl_0.05-1.debian.tar.xz
cd %{_builddir}/Proc-Wait3-0.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Proc-Wait3-0.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Proc-Wait3
cp %{_builddir}/Proc-Wait3-0.05/LICENSE %{buildroot}/usr/share/package-licenses/perl-Proc-Wait3/2753674007440763253a8aa3a876c81ac7f6e52c
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Proc-Wait3/036d6a142aa700c9543dbdb6d5afb2cfe52ec4ad
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Proc::Wait3.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Proc-Wait3/036d6a142aa700c9543dbdb6d5afb2cfe52ec4ad
/usr/share/package-licenses/perl-Proc-Wait3/2753674007440763253a8aa3a876c81ac7f6e52c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Proc/Wait3.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Proc/Wait3/Wait3.so
