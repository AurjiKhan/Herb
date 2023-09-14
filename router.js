import HomeComponent from "@/components/HomeComponent.vue";
import SignComponent from "@/components/SignComponent.vue";

import {createRouter,createWebHistory} from 'vue-router'

import MintComponent from "@/components/MintComponent.vue";
import ThymeComponent from "@/components/ThymeComponent.vue";
import BasilComponent from "@/components/BasilComponent.vue";
import LavenderComponent from "@/components/LavenderComponent.vue";
import ChamomileComponent from "@/components/ChamomileComponent.vue";
import PaymentComponent from "@/components/PaymentComponent.vue";
import loginComponent from "@/components/loginComponent.vue";
import ViewCart from "@/components/ViewCart.vue";

const routes=[
    {
        name:'HomeComponent',
        component:HomeComponent,
        path:'/'
    },
    {
        name: 'SignComponent',
        component:SignComponent,
        path:'/SignComponent'
    },
    {
    path: '/cart', // Define the route for the "View Cart" page
    name: 'ViewCart',
    component: ViewCart
  },
    {
        name:'Mint',
        component:MintComponent,
        path:'/MintComponent'
    },
      {
        name:'Thyme',
        component:ThymeComponent,
        path:'/ThymeComponent'
    },
      {
        name:'Basil',
        component:BasilComponent,
        path:'/BasilComponent'
    },
      {
        name:'Lavender',
        component:LavenderComponent,
        path:'/LavenderComponent'
    },
      {
        name:'Chamomile',
        component:ChamomileComponent,
        path:'/ChamomileComponent'
    },
       {
        name:'PaymentComponent',
        component:PaymentComponent,
        path:'/PaymentComponent'
    },
      {
        name:'loginComponent',
        component:loginComponent,
        path:'/loginComponent'
    },


];

const router = createRouter({
    history:createWebHistory(),
    routes,
});

export default router;