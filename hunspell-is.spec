Name: hunspell-is
Summary: Icelandic hunspell dictionaries
%define upstreamid 20090823
Version: 0.%{upstreamid}
Release: 1.1%{?dist}
Source: http://extensions.services.openoffice.org/files/2829/1/Icelandic-dict-2009-08-23.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/dict-is
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Icelandic hunspell dictionaries.

%prep
%setup -q -c -n hunspell-is

%build
for i in LICENSE_en_US.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/is_IS.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE_en_US.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090823-1.1
- Rebuilt for RHEL 6

* Tue Aug 25 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090823-1
- most recent effort

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060928-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20060928-4
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060928-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060928-2
- Duplicate dictionaries installed

* Wed Sep 03 2006 Caolan McNamara <caolanm@redhat.com> - 0.20060928-1
- initial version
