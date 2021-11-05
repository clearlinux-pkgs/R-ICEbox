#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ICEbox
Version  : 1.1.2
Release  : 27
URL      : https://cran.r-project.org/src/contrib/ICEbox_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ICEbox_1.1.2.tar.gz
Summary  : Individual Conditional Expectation Plot Toolbox
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-sfsmisc
BuildRequires : R-sfsmisc
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n ICEbox
cd %{_builddir}/ICEbox

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589781542

%install
export SOURCE_DATE_EPOCH=1589781542
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICEbox
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICEbox
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICEbox
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ICEbox || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ICEbox/CITATION
/usr/lib64/R/library/ICEbox/DESCRIPTION
/usr/lib64/R/library/ICEbox/INDEX
/usr/lib64/R/library/ICEbox/Meta/Rd.rds
/usr/lib64/R/library/ICEbox/Meta/data.rds
/usr/lib64/R/library/ICEbox/Meta/features.rds
/usr/lib64/R/library/ICEbox/Meta/hsearch.rds
/usr/lib64/R/library/ICEbox/Meta/links.rds
/usr/lib64/R/library/ICEbox/Meta/nsInfo.rds
/usr/lib64/R/library/ICEbox/Meta/package.rds
/usr/lib64/R/library/ICEbox/NAMESPACE
/usr/lib64/R/library/ICEbox/R/ICEbox
/usr/lib64/R/library/ICEbox/R/ICEbox.rdb
/usr/lib64/R/library/ICEbox/R/ICEbox.rdx
/usr/lib64/R/library/ICEbox/data/WhiteWine.RData
/usr/lib64/R/library/ICEbox/help/AnIndex
/usr/lib64/R/library/ICEbox/help/ICEbox.rdb
/usr/lib64/R/library/ICEbox/help/ICEbox.rdx
/usr/lib64/R/library/ICEbox/help/aliases.rds
/usr/lib64/R/library/ICEbox/help/paths.rds
/usr/lib64/R/library/ICEbox/html/00Index.html
/usr/lib64/R/library/ICEbox/html/R.css
