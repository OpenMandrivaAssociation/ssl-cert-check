Summary:	SSL certificate expiration checker
Name:		ssl-cert-check
Version:	3.3
Release:	4
License:	BSD-like
Group:		Monitoring
URL:		http://prefetch.net/code/ssl-cert-check.html
Source0:	http://prefetch.net/code/ssl-cert-check.bz2
Patch0:		ssl-cert-check-3.3-mdv_conf.diff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ssl-cert-check is a utility for checking the expiration date of an X.509
certificate. ssl-cert-check can be run against a live server or a PEM encoded
digital certificate.

%prep

%setup -q -c -T
bzcat %{SOURCE0} > %{name}
%patch0 -p0

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.3-3mdv2010.0
+ Revision: 434106
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3-2mdv2009.0
+ Revision: 239027
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 3.3-1mdv2008.0
+ Revision: 83822
- Import ssl-cert-check



* Tue Aug 22 2006 Oden Eriksson <oeriksson@mandriva.com> 3.3-1mdv2007.0
- initial Mandriva package
