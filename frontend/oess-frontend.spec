Name:		oess-frontend
Version:	1.1.5
Release:	1%{?dist}
Summary:	The core oess service provides

Group:		Network
License:	APL 2.0
URL:		http://www.grnoc.iu.edu	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	perl
Requires:	perl-OESS >= 1.1.5, perl(Net::DBus),dbus,dbus-libs,mysql-server,oess-core
Requires:       nox >= 0.10.5
Requires:       yui2
Requires:       httpd, mod_ssl
Requires:       nddi-tiles
Requires:	perl-Crypt-SSLeay
Requires:	xmlsec1
Requires:	xmlsec1-openssl
BuildArch:	noarch
%description


%define destdir %{_datadir}/%{name}/

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p -m 0755 %{buildroot}/%{_datadir}/%{name}/
%{__mkdir} -p -m 0755 %{buildroot}/%{_datadir}/%{name}/www/
%{__mkdir} -p -m 0755 %{buildroot}/%{_datadir}/%{name}/www/openlayers
%{__mkdir} -p -m 0755 %{buildroot}/%{_datadir}/%{name}/webservice/
%{__mkdir} -p -m 0755 %{buildroot}/%{_datadir}/%{name}/conf/
%{__mkdir} -p -m 0755 %{buildroot}/%{_datadir}/%{name}/docs/
%{__mkdir} -p -m 0755 %{buildroot}/etc/httpd/conf.d/


cp -ar www/admin %{buildroot}%{destdir}/www/
cp -ar www/css %{buildroot}%{destdir}/www/
cp -ar www/html_templates %{buildroot}%{destdir}/www/
cp -ar www/index.cgi %{buildroot}%{destdir}/www/
cp -ar www/js_templates %{buildroot}%{destdir}/www/
cp -ar www/js_utilities %{buildroot}%{destdir}/www/
cp -ar www/media %{buildroot}%{destdir}/www/
cp -ar www/openlayers/OpenLayers.js %{buildroot}%{destdir}/www/openlayers
cp -ar webservice/* %{buildroot}%{destdir}/webservice/
cp -ar conf/* %{buildroot}%{destdir}/conf/
cp -ar docs/* %{buildroot}%{destdir}/docs/

%{__install} conf/oe-ss.conf.example %{buildroot}/etc/httpd/conf.d/oe-ss.conf

find . -type f | sed 's:./:%{destdir}/:' |grep -v spec |grep -v Makefile > $RPM_BUILD_DIR/file.list.%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f ../file.list.%{name}

%config(noreplace) /etc/httpd/conf.d/oe-ss.conf


%doc

%post
mkdir -p %{_sysconfdir}/oess/
mkdir -p /var/run/oess/
chmod a+rw /var/run/oess/

%changelog

