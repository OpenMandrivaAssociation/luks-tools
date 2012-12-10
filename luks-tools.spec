Summary: Utilities for working with LUKS-protected filesystems
Name: luks-tools
Version: 0.0.14
Release: %mkrel 1
License: GPL
Group: File tools
Source0: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.gz
# (fc) 0.0.12-1mdv fix pam-stack deprecated usage
Patch0: luks-tools-0.0.12-fixpamstack.patch
# (fc) 0.0.12-1mdv fix consolehelper file
Patch1: luks-tools-0.0.12-fixconsolehelper.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.flyn.org
Requires: cryptsetup-luks
Requires: usermode
# These three are needed for gnome-luks-format - AdamW 2008/02
Requires: python-dbus
Requires: pygtk2.0
Requires: pygtk2.0-libglade
BuildRequires: cryptsetup-luks
BuildRequires: glib2-devel
BuildRequires: libuuid-devel

%description
The luks-tools package contains various utilities for working with 
LUKS-protected filesystems. HAL uses these utilites to automatically 
mount encrypted volumes when they are attached to a system, provided 
the user can produce the correct passphrase. These utilities are 
written as separate programs to allow MAC systems like SELinux to 
have fine-grained control over them.

luks-format
    A utility that formats a filesystem to contain a LUKS encryption 
    header.

luks-is-encrypted
    A tool that can determine if a filesystem contains a LUKS 
    encryption header.

luks-setup
    A utility that sets up the dm-crypt device map for a partition.

gnome-luks-format
    A GNOME front-end for luks-format.



%prep
%setup -q
%patch0 -p1 -b .fixpamstack
%patch1 -p1 -b .fixconsolehelper

%build
PATH="$PATH:/sbin" %configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mv $RPM_BUILD_ROOT%{_bindir}/gnome-luks-format $RPM_BUILD_ROOT%{_sbindir}/gnome-luks-format 
ln -s consolehelper $RPM_BUILD_ROOT%{_bindir}/gnome-luks-format 

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ
%{_sysconfdir}/pam.d/*
%{_sysconfdir}/security/console.apps/*
%{_datadir}/luks-tools/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*


%changelog
* Wed Mar 16 2011 Funda Wang <fwang@mandriva.org> 0.0.14-1mdv2011.0
+ Revision: 645379
- BR uuid

  + Stéphane Téletchéa <steletch@mandriva.org>
    - update to new version 0.0.14

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Thu Jul 30 2009 Frederic Crozat <fcrozat@mandriva.com> 0.0.13-1mdv2010.0
+ Revision: 404628
- Release 0.0.13

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.0.12-4mdv2009.0
+ Revision: 251556
- rebuild

* Wed Feb 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.0.12-2mdv2008.1
+ Revision: 175941
- add some requires without which gnome-luks-format doesn't work

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 29 2007 Frederic Crozat <fcrozat@mandriva.com> 0.0.12-1mdv2008.0
+ Revision: 32551
- Fix buildrequires
- Release 0.0.12
- Patch0: fix pam-stack obsolete usage
- Patch1: fix consolehelper/usermode usage
- Import luks-tools



* Mon Sep 11 2006 Frederic Crozat <fcrozat@mandriva.com> 0.0.11-1mdv2007.0
- Initial Mandriva release
