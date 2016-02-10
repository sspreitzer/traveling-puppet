Name:		traveling-puppet
Version:	3.8.4
Release:	4
Summary:	traveling puppet

Group:		System Environment/Base
License:	ASL 2.0
URL:		https://github.com
Source:		%{name}-%{version}.tar.gz

# There is a need to fix the paths
# to make traveling puppet work
# out of the box
Patch0:		traveling-puppet.dirfix.patch

AutoReq:	no
AutoProv:	no

BuildArch:	x86_64

%description
Traveling Puppet for 64bit Gnu/Linux
Based on traveling-ruby

%prep
%autosetup -p1

%install
%{__mkdir_p} %{buildroot}%{_usr}/share/%{name}
%{__mkdir_p} %{buildroot}%{_usr}/bin
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}/modules
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}/hiera
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/%{name}

%{__cp} -vr %{_builddir}/%{name}-%{version}/* %{buildroot}%{_usr}/share/%{name}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}
cat << EOF >> %{buildroot}%{_sysconfdir}/%{name}/puppet.conf
[main]
confdir=%{_sysconfdir}/%{name}
vardir=%{_sharedstatedir}/%{name}
EOF

cat << EOF >> %{buildroot}%{_sysconfdir}/%{name}/hiera.yaml
---
:backends: yaml
:yaml:
  :datadir: %{_sysconfdir}/%{name}/hiera
:hierarchy: common
:logger: console
EOF

for i in $(ls %{buildroot}%{_usr}/share/%{name}/scripts); do
  %{__ln_s} %{_usr}/share/%{name}/scripts/${i} %{buildroot}%{_usr}/bin/${i}
done

%files
%{_usr}/bin/*
%{_usr}/share/%{name}
%{_sharedstatedir}/%{name}
%config %{_sysconfdir}/%{name}/*

%changelog
* Sun Feb 02 2016 Sascha Spreitzer <sspreitz@redhat.com> - 3.8.4-4
- Major refactoring
* Mon Jan 25 2016 Sascha Spreitzer <sspreitz@redhat.com> - 3.8.4-3
- Changes sources to standard artifacts by conventions
* Fri Jan 15 2016 Sascha Spreitzer <sspreitz@redhat.com> - 3.8.4-2
- Add Puppet config
* Wed Jan 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 3.8.4-1
- Pin to puppet version
* Wed Jan 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1-1
- Initial creation
