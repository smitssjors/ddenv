# Docker Dev Environment

## Usage
`ddenv` -> always read config from file if there is one

`ddenv --config ./walla/ddenv.yml` -> specify config file

`ddenv node index.js` -> try to infer the runtime

`ddenv -r node -v 12 node index.js` -> specify runtime and runtime version
