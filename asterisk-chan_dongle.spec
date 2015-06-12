%define	snap	20150612
Summary:	Asterisk huawei 3g dongle channel driver
Name:		asterisk-chan_dongle
Version:	1.1
Release:	0.%{snap}.1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/bg111/asterisk-chan-dongle/archive/master.zip
# Source0-md5:	8527ea21c083821fb0bd69c834d17737
Patch0:		chan_dongle-pin.patch
URL:		http://wiki.e1550.mobi/
BuildRequires:	asterisk-devel >= 1.8
BuildRequires:	asterisk-devel < 1.9
Requires:	usb-modeswitch
Requires:	usb-modeswitch-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chan_dongle is an Asterisk channel driver for Huawei UMTS/3G USB
modems (dongles). At this moment, the supported features are:

- Voice calls, dialling by modem name, group, round robin, provider
  name, IMEI or IMSI.
- Call waiting
- Call holding
- Conference (multiparty) call
- Send SMS from CLI, asterisk manager and dialplan
- Receive SMS (latin charset and multiline included)
- Send USSD
- Receive USSD (latin charset and multiline included)
- Send DTMF (excluding A,B,C,D letters not supported by Huawei)
- Receive DTMF

%prep
%setup -q -n asterisk-chan-dongle-master
%patch0 -p1

%build
install /usr/share/automake/{config.*,install-sh,missing} .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D etc/dongle.conf $RPM_BUILD_ROOT%{_sysconfdir}/asterisk/dongle.conf
install -D chan_dongle.so $RPM_BUILD_ROOT%{_libdir}/asterisk/modules/chan_dongle.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README.txt TODO.txt etc/extensions.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_dongle.so
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/dongle.conf
