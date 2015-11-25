Name:           ros-indigo-dna-extraction-msgs
Version:        0.0.5
Release:        1%{?dist}
Summary:        ROS dna_extraction_msgs package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation

%description
Message definitions for controlling DNA extraction related actions in the ACAT
project context

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 25 2015 Ferenc Balint-Benczedi <balintbe@cs.uni-bremen.de> - 0.0.5-1
- Autogenerated by Bloom

* Fri Apr 24 2015 Ferenc Balint-Benczedi <balintbe@cs.uni-bremen.de> - 0.0.5-0
- Autogenerated by Bloom

* Thu Mar 19 2015 Ferenc Balint-Benczedi <balintbe@cs.uni-bremen.de> - 0.0.4-0
- Autogenerated by Bloom

* Wed Dec 10 2014 ferenc <ferenc@todo.todo> - 0.0.3-1
- Autogenerated by Bloom

* Tue Oct 14 2014 ferenc <ferenc@todo.todo> - 0.0.3-0
- Autogenerated by Bloom

