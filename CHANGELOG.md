## [1.6.2](https://github.com/egshiglen2024359/capstone-project/compare/v1.6.1...v1.6.2) (2025-08-08)

### Bug Fixes

* **ingress:** route /static (and /media) to app so DRF assets load via Ingress ([47d030f](https://github.com/egshiglen2024359/capstone-project/commit/47d030f12b33948b1d3ed8a8e48acb39acde8052))
* **ingress:** route /static (and /media) to app so DRF assets load via Ingress ([7a37801](https://github.com/egshiglen2024359/capstone-project/commit/7a37801330f48c786c74dc2f71a5658c65833322))

## [1.6.1](https://github.com/egshiglen2024359/capstone-project/compare/v1.6.0...v1.6.1) (2025-08-08)

### Bug Fixes

* **ingress:** correct path configuration for application routing ([9c1a6a6](https://github.com/egshiglen2024359/capstone-project/commit/9c1a6a6631bb0453421d9274af2bced114111184))

## [1.6.0](https://github.com/egshiglen2024359/capstone-project/compare/v1.5.2...v1.6.0) (2025-08-08)

### Features

* **api:** add serializer validations and test for future published_date  ([9b2854a](https://github.com/egshiglen2024359/capstone-project/commit/9b2854acf3f20b88789ef3f326f53f8c2d4f5cd9))
* **serializer:** add ISBN and published_date validation with text trimming ([ced8937](https://github.com/egshiglen2024359/capstone-project/commit/ced893792598b1a1197c97a8333d0f728c67324c))

## [1.5.2](https://github.com/egshiglen2024359/capstone-project/compare/v1.5.1...v1.5.2) (2025-08-08)

### Bug Fixes

* **helm:** change books.local to localhost on values.yaml and app version to 1.16.0 on chart ([8742a77](https://github.com/egshiglen2024359/capstone-project/commit/8742a773b3bec6f3f67cf9c30dddedead589d3ca))
* **helm:** change books.local to localhost on values.yaml and app version to 1.16.0 on chart ([9d481df](https://github.com/egshiglen2024359/capstone-project/commit/9d481dff61834052c39c59dc031cc35dc713fa2a))
* **helm:** change books.local to localhost on values.yaml and app version to 1.16.0 on chart ([5ecedb1](https://github.com/egshiglen2024359/capstone-project/commit/5ecedb13a196da4ef05f14150ecb9132c6cd1369))

## [1.5.1](https://github.com/egshiglen2024359/capstone-project/compare/v1.5.0...v1.5.1) (2025-08-07)

### Bug Fixes

* **helm:** update ingress host to books.local for local access ([37a057a](https://github.com/egshiglen2024359/capstone-project/commit/37a057a220264c3cb58df82830fa6f25f5a7849a))

## [1.5.0](https://github.com/egshiglen2024359/capstone-project/compare/v1.4.3...v1.5.0) (2025-08-07)

### Features

* Adding new deployment job on workflow and testing ([cf3db76](https://github.com/egshiglen2024359/capstone-project/commit/cf3db76b3fe8a70858d5f36c253a558f0fd5490d))

## [1.4.3](https://github.com/egshiglen2024359/capstone-project/compare/v1.4.2...v1.4.3) (2025-08-07)

### Bug Fixes

* **helm:** set image tag to 1.4.2 for production [skip ci] ([5ccc69b](https://github.com/egshiglen2024359/capstone-project/commit/5ccc69b1d8bf3036436cf07c88c69995b8927241))

## [1.4.2](https://github.com/egshiglen2024359/capstone-project/compare/v1.4.1...v1.4.2) (2025-08-07)

### Bug Fixes

* **ingress:** correct Ingress rule structure to resolve ArgoCD OutOfSync issue ([461bb0e](https://github.com/egshiglen2024359/capstone-project/commit/461bb0e5e25e839b337026267e9aa90e6650443d))

## [1.4.1](https://github.com/egshiglen2024359/capstone-project/compare/v1.4.0...v1.4.1) (2025-08-07)

### Bug Fixes

* **ingress:** add host field to fix ArgoCD OutOfSync issue ([c6d5c41](https://github.com/egshiglen2024359/capstone-project/commit/c6d5c4120e1479b225e040a2f5d2906ed4ea98c9))

## [1.4.0](https://github.com/egshiglen2024359/capstone-project/compare/v1.3.1...v1.4.0) (2025-08-06)

### Features

* **helm:** add ingress config and update persistence for ArgoCD ([3dde1de](https://github.com/egshiglen2024359/capstone-project/commit/3dde1def5a2412f7257b4a841f5e60098af0b8a3))

## [1.3.1](https://github.com/egshiglen2024359/capstone-project/compare/v1.3.0...v1.3.1) (2025-08-06)

### Bug Fixes

* **ci:** correct semantic-release output variable names to enable Docker build job ([3c9df2f](https://github.com/egshiglen2024359/capstone-project/commit/3c9df2fc09c7eafdb0aec979fc4125e3dc10e7da))

## [1.3.0](https://github.com/egshiglen2024359/capstone-project/compare/v1.2.0...v1.3.0) (2025-08-06)

### Features

* **ci:** verify full CI/CD pipeline with semantic-release and docker build ([bac4085](https://github.com/egshiglen2024359/capstone-project/commit/bac40852fb24fe383b2e1484cd4a43f49c2d23f8))

## [1.2.0](https://github.com/egshiglen2024359/capstone-project/compare/v1.1.0...v1.2.0) (2025-08-01)

### Features

* **ci:** test semantic release workflow ([ea4bd08](https://github.com/egshiglen2024359/capstone-project/commit/ea4bd089e55ba3321790d99f29a39a14ba5ac31f))

## [1.1.0](https://github.com/egshiglen2024359/capstone-project/compare/v1.0.0...v1.1.0) (2025-08-01)

### Features

* **ci:** trigger new release for testing ([4d99e94](https://github.com/egshiglen2024359/capstone-project/commit/4d99e941436d7d92f84d4545d46390e163ed2536))

## 1.0.0 (2025-08-01)

### Features

* add Book model with title, author, ISBN, published date ([5ccf81c](https://github.com/egshiglen2024359/capstone-project/commit/5ccf81c27f509c21e22a4f735709df205b765e9e))
* add initial migration for book model ([2b33a69](https://github.com/egshiglen2024359/capstone-project/commit/2b33a69b0ceb285c696b2379c55214b249be66b8))
* add semantic-release ([bc36c0d](https://github.com/egshiglen2024359/capstone-project/commit/bc36c0d8596a0c7e11dc3556444b8a916bde6f8d))
* add semantic-release ([0d13b6e](https://github.com/egshiglen2024359/capstone-project/commit/0d13b6ea7cf4226749cc308eacdd2bbc7344506a))
* **api:** add BookView and BookDetailView with URL routes and comments ([21383c0](https://github.com/egshiglen2024359/capstone-project/commit/21383c073b2b4e20f73db19ac3db0cf1cc31f112))
* **api:** add checked out status on Book model ([16f14de](https://github.com/egshiglen2024359/capstone-project/commit/16f14deae8800c9fec1433a008e3804d240a7520))
* **api:** add health check endpoint ([5c1fffb](https://github.com/egshiglen2024359/capstone-project/commit/5c1fffbdd32efa7c42c2c7aa35edf88fe981c3b2))
* **api:** add pytest for health view ([d4a480a](https://github.com/egshiglen2024359/capstone-project/commit/d4a480a6e84d8486984bf3babf626b43c797b527))
* **api:** add status, timestamps, ISBN validation, and ordering to Book model, update serializer ([bf29d74](https://github.com/egshiglen2024359/capstone-project/commit/bf29d7487c5f23416ba1d65b12c829bcb867a4c2))
* **api:** expose book ID in serializer and update tests ([702442c](https://github.com/egshiglen2024359/capstone-project/commit/702442c96a3ae685298dd3b8df8a98982cff6353))
* configure URL routes for book list, create, retrieve, update, & delete ([30c4bab](https://github.com/egshiglen2024359/capstone-project/commit/30c4babbeb35a70f99def32f5c511f1531cf6e6b))
* create BookSerializer for model serialization and validation ([42f3f83](https://github.com/egshiglen2024359/capstone-project/commit/42f3f83cbb5e06d60e90ebc871b24f8e94fb0343))
* **helm:** add Kubernetes Helm Chart for Django and database ([7a17b93](https://github.com/egshiglen2024359/capstone-project/commit/7a17b934af3ece37efe0009d37ebce31983f03eb))
* **helm:** add Kubernetes Helm Chart for Django and database ([83f95fe](https://github.com/egshiglen2024359/capstone-project/commit/83f95fe7f8e0af8305632c8b830176bb1be61bce))
* **helm:** add migration job hook and update congifmap for automated database migrations ([f62bc96](https://github.com/egshiglen2024359/capstone-project/commit/f62bc9683c0cbb2bfbe0c3f9b36f5253516afd5b))
* **helm:** add migration job hook and update congifmap for automated database migrations  ([43fef74](https://github.com/egshiglen2024359/capstone-project/commit/43fef747fc373a328ce5d9a32e5c99d8014f7d61))
* implement APIView based CRUD for book catalog ([beec477](https://github.com/egshiglen2024359/capstone-project/commit/beec477243cb39f75ae686eb545dfe3b068f0d31))
* initialisation of django project ([f1b2474](https://github.com/egshiglen2024359/capstone-project/commit/f1b247462fa394c408d590b970fa2103a0a77f3a))

### Bug Fixes

* **django:** allow all hosts for Kubernetes testing ([2560545](https://github.com/egshiglen2024359/capstone-project/commit/25605451475837d7a626dad1a3586ff5f5b7c1ea))
* **docker:** correct LABEL metadata ([48c8675](https://github.com/egshiglen2024359/capstone-project/commit/48c86758f3fb4dbd564f53f0bc668258177b4091))
* **docker:** solve migration handling issue in entrypoint script and Dockerfile ([ab0b920](https://github.com/egshiglen2024359/capstone-project/commit/ab0b920c2da364e53a161437057f6254f66d1a0b))
* update book endpoint URL name for reverse lookup in tests ([10ea4fe](https://github.com/egshiglen2024359/capstone-project/commit/10ea4fe7e5f460e5c8f0db2993aff106701d41d0))
* **workflow:** remove env ([46cd510](https://github.com/egshiglen2024359/capstone-project/commit/46cd510af53d773788bbf2cb7cba7a4cb759a934))
* **workflow:** remove env complete ([a0436d7](https://github.com/egshiglen2024359/capstone-project/commit/a0436d77ed28c81938bb74858580d91e4a8d30a8))
* **workflow:** remove envs ([5df8893](https://github.com/egshiglen2024359/capstone-project/commit/5df88937d1e213653c95f132ccf5b81db832c67d))
