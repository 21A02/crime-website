"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _wrapNativeSuper(Class) { var _cache = typeof Map === "function" ? new Map() : undefined; _wrapNativeSuper = function _wrapNativeSuper(Class) { if (Class === null || !_isNativeFunction(Class)) return Class; if (typeof Class !== "function") { throw new TypeError("Super expression must either be null or a function"); } if (typeof _cache !== "undefined") { if (_cache.has(Class)) return _cache.get(Class); _cache.set(Class, Wrapper); } function Wrapper() { return _construct(Class, arguments, _getPrototypeOf(this).constructor); } Wrapper.prototype = Object.create(Class.prototype, { constructor: { value: Wrapper, enumerable: false, writable: true, configurable: true } }); return _setPrototypeOf(Wrapper, Class); }; return _wrapNativeSuper(Class); }

function isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Date.prototype.toString.call(Reflect.construct(Date, [], function () {})); return true; } catch (e) { return false; } }

function _construct(Parent, args, Class) { if (isNativeReflectConstruct()) { _construct = Reflect.construct; } else { _construct = function _construct(Parent, args, Class) { var a = [null]; a.push.apply(a, args); var Constructor = Function.bind.apply(Parent, a); var instance = new Constructor(); if (Class) _setPrototypeOf(instance, Class.prototype); return instance; }; } return _construct.apply(null, arguments); }

function _isNativeFunction(fn) { return Function.toString.call(fn).indexOf("[native code]") !== -1; }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

var MyHeader =
/*#__PURE__*/
function (_HTMLElement) {
  _inherits(MyHeader, _HTMLElement);

  function MyHeader() {
    _classCallCheck(this, MyHeader);

    return _possibleConstructorReturn(this, _getPrototypeOf(MyHeader).apply(this, arguments));
  }

  _createClass(MyHeader, [{
    key: "connectedCallback",
    value: function connectedCallback() {
      this.innerHTML = "\n<header class=\"navbar navbar-nav navbar-expand navbar-light navbar-theme-primary\">\n<div class=\"container-fluid px-3 px-md-4\">\n\n\n  <!-- -----------------website name and icon-------------- -->\n\n  <div class=\"d-flex align-item pt-2 pb-2 pr-2s-center\">\n    <a class=\"navbar-brand shadow-soft py-2 px-3 rounded border border-light mr-xl-4\" href=\"#\">\n\n      <span class=\"ml-2 text-dark\" style=\"font-size: large;\"><i class=\"fas fa-chart-pie\"></i>&nbsp &nbsp Crime Data\n        Analytics</span>\n    </a>\n  </div>\n\n  <!-- ---------------------nav-bar-item pt-2 pb-2 pr-2s---------------------------- -->\n  <div class=\"d-flex align-item pt-2 pb-2 pr-2s-center\">\n    <div class=\"d-none d-lg-block\">\n      <a href=\"index.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-home\"></i>&nbsp Home</a>\n      <a href=\"crime-charts.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-globe-asia\"></i>&nbsp CrimeCharts</a>\n      <a href=\"crime-predictor.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-robot\"></i>&nbsp CrimePredictor</a>  \n      <a href=\"crime-locator.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-map-marker-alt\"></i> &nbsp CrimeLocator</a>\n      <a href=\"feed.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-newspaper\"></i>&nbsp CrimeFeed</a>\n      <a href=\"about.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-user-secret\"></i>&nbsp About Us</a>\n      <a href=\"help-page.html\" class=\"btn btn-primary text-dark mr-2\"><i class=\"fas fa-info-circle\"></i>&nbsp Help</a>\n    </div>\n  </div>\n\n  <a href=\"#\" class=\"btn-emoji\" onclick=\"audio()\">\n    <i class=\"far fa-grin-tongue\"></i>\n  </a>\n\n\n  <div id=\"txt\"> </div>\n\n</div>\n\n<script src=\"https://kit.fontawesome.com/7bdcd846e8.js\" crossorigin=\"anonymous\"></script>\n\n\n";
    }
  }]);

  return MyHeader;
}(_wrapNativeSuper(HTMLElement));

customElements.define('my-header', MyHeader);

var MyFooter =
/*#__PURE__*/
function (_HTMLElement2) {
  _inherits(MyFooter, _HTMLElement2);

  function MyFooter() {
    _classCallCheck(this, MyFooter);

    return _possibleConstructorReturn(this, _getPrototypeOf(MyFooter).apply(this, arguments));
  }

  _createClass(MyFooter, [{
    key: "connectedCallback",
    value: function connectedCallback() {
      this.innerHTML = "\n<footer>\n<div class=\"row pt-5 mx-auto\" style=\"\nposition: absolute;\nbottom: 5;\nleft: 0;\nright: 0;\ndisplay: flex;\nflex-direction: row;\nflex-wrap: nowrap;\nalign-content: center;\njustify-content: center;\nalign-items: center;\">\n    <div class=\"col-3 \"><i class=\"fas fa-copyright\"></i> 2021 Crime Data Analysis All rights reserved </div>\n</div>\n</footer>\n\n\n";
    }
  }]);

  return MyFooter;
}(_wrapNativeSuper(HTMLElement));

customElements.define('my-footer', MyFooter);