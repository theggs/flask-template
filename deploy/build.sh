set -xe

fetch(){
  git pull
}

build(){
  version=`git describe --always`
  sudo docker build . -f ./deploy/Dockerfile -t reigstry:$version
  sudo docker push reigstry:$version
}

fetch
build
