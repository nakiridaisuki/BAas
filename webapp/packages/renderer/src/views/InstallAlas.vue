<template>
  <div class="w-full h-full flex justify-center items-center flex-col">
    <AlasTitle />
    <section class="mt-5 w-148">
      <a-form
        class="alas-install flex-auto w-full justify-between"
        layout="inline"
        :label-col="{style: 'width: 100px'}"
        :label-align="'left'"
        :model="configForm"
      >
        <a-form-item
          :wrapper-col="{style: 'width: 100%'}"
          :label="t('common.language')"
          name="language"
        >
          <a-select
            v-model="configForm.language"
            :options="localeList"
            @change="selectLanguage"
          />
        </a-form-item>
        <a-form-item
          :wrapper-col="{span: 16}"
          :label="t('common.update')"
          name="repository"
        >
          <a-select
            v-model="configForm.repository"
            :options="repositoryOptions"
            @change="selectRepository"
          />
        </a-form-item>
        <a-form-item
          :wrapper-col="{span: 16}"
          :label="t('common.theme')"
          name="theme"
        >
          <a-select
            v-model="configForm.theme"
            :options="themeOptions"
            @change="selectTheme"
          />
        </a-form-item>
      </a-form>
      <div class="w-full text-end">
        <a-button
          type="link"
          class="text-end cursor-pointer p-0 install-tips"
          :onclick="goToImportPage"
        >
          <a-typography-text>
            {{ t('common.installTips') }}
          </a-typography-text>
        </a-button>
      </div>
    </section>
    <AButton
      type="primary"
      size="large"
      class="!mt-16 !w-48 !h-16 !bg-primary !rounded-xl"
      :onclick="installAlas"
      :loading="installLoading"
    >
      <a-typography-text class="text-2xl !text-current !dark:text-dark">
        {{ t('common.install') }}
      </a-typography-text>
    </AButton>
  </div>
</template>

<script lang="ts" setup>
import AlasTitle from '/@/components/AlasTitle.vue';
import {useI18n} from '/@/hooks/useI18n';
import {computed, ref, unref} from 'vue';
import {localeList} from '/@/settings/localSetting';
import {useAppStoreWithOut} from '/@/store/modules/app';
import type {LocaleType, ThemeVal} from '/#/config';
import {setupThemeSetting} from '/@/settings/themeSetting';
import {useLocale} from '/@/locales/useLocale';
import router from '/@/router';
import {AlasGuiTheme} from '@common/constant/theme';
import {repositoryMap} from '/@/settings/repositorySeeing';

const {t} = useI18n();
const appStore = useAppStoreWithOut();
const {changeLocale} = useLocale();

const installLoading = ref<boolean>(false);

const configForm = ref<{
  language: LocaleType;
  repository: string;
  theme: ThemeVal;
}>({
  language: unref(appStore.getLanguage),
  repository: unref(appStore.getRepository),
  theme: unref(appStore.getTheme) as ThemeVal,
});

const repositoryOptions = computed(() => [
  {
    label: t('common.global'),
    value: 'global',
  },
  // {
  //   label: t('common.china'),
  //   value: 'china',
  // },
]);

const themeOptions = computed(() => [
  {
    label: t('common.light'),
    value: 'light',
  },
  {
    label: t('common.dark'),
    value: 'dark',
  },
]);

const selectLanguage = (value: LocaleType) => {
  appStore.setLanguage(value);
  changeLocale(value);
};
const selectRepository = (value: string) => {
  appStore.setRepository(value);
};
const selectTheme = (value: ThemeVal) => {
  appStore.setTheme(value);
  setupThemeSetting(value);
};

const goToImportPage = () => {
  router.push('/import');
};

const installAlas = async () => {
  installLoading.value = true;
  const modifyConfig = {
    Language: unref(appStore.getLanguage),
    Repository: repositoryMap[unref(appStore.getRepository)],
    Theme: AlasGuiTheme[unref(appStore.theme)],
  };
  const filePath = unref(appStore.alasPath);
  window.__electron_preload__modifyConfigYaml(filePath, modifyConfig);
  installLoading.value = false;
  router.push('/Launch');
};
</script>

<style lang="less" scoped>
.alas-install {
  :deep(.arco-select-view-single) {
    min-width: 120px;
    background: var(--color-bg);
    border-left: none;
    border-right: none;
    border-top: none;
    border-bottom: 2px solid rgb(var(--primary-6));
    border-radius: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;

    .arco-select-view-value {
      justify-content: center;
    }

    .arco-select-view-suffix {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);

      .arco-select-view-arrow-icon {
        transition: ease-in-out 0.2s;
      }
    }
  }

  .arco-form-item-layout-inline {
    margin-right: 0;
  }
}
</style>
