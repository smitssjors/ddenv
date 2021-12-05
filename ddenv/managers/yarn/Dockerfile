ARG VERSION
FROM node:$VERSION as build

WORKDIR /app

COPY package.json .
COPY yarn.lock .

RUN yarn

FROM node:$VERSION

WORKDIR /app

COPY --from=build /app/node_modules .
